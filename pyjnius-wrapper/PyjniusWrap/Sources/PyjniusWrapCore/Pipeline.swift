import Foundation
import PySwiftAST
import PySwiftCodeGen

/// Orchestrates: `[input dir] -> JAR -> JSON -> AstDocument -> Python files`.
public struct Pipeline {

    public struct Options {
        public var inputDir: URL
        public var outputDir: URL
        public var jarPath: URL
        public var javaExecutable: String
        public var fileLayout: FileLayout

        public init(inputDir: URL, outputDir: URL, jarPath: URL,
                    javaExecutable: String = "java",
                    fileLayout: FileLayout = .perClass) {
            self.inputDir = inputDir
            self.outputDir = outputDir
            self.jarPath = jarPath
            self.javaExecutable = javaExecutable
            self.fileLayout = fileLayout
        }
    }

    /// Output layout strategy.
    public enum FileLayout {
        /// One `.py` file per class, mirroring the Java package hierarchy.
        case perClass
        /// All classes flattened into a single file (debug helper).
        case singleFile
    }

    public enum PipelineError: Error, CustomStringConvertible {
        case javaFailed(exitCode: Int32, stderr: String)
        case decodeFailed(String)

        public var description: String {
            switch self {
            case .javaFailed(let code, let err):
                return "java-ast-emitter exited \(code): \(err)"
            case .decodeFailed(let msg):
                return "AST JSON decode failed: \(msg)"
            }
        }
    }

    public init() {}

    public func run(_ opts: Options) throws -> [URL] {
        let json = try invokeJar(opts: opts)
        let doc: AstDocument
        do {
            doc = try JSONDecoder().decode(AstDocument.self, from: json)
        } catch {
            throw PipelineError.decodeFailed(String(describing: error))
        }
        return try emit(doc: doc, opts: opts)
    }

    /// Decoupled hook so tests can feed a pre-baked AST without launching the JVM.
    public func emit(doc: AstDocument, opts: Options) throws -> [URL] {
        let emitter = PyWrapperEmitter()
        try FileManager.default.createDirectory(at: opts.outputDir,
                                                withIntermediateDirectories: true)
        var written: [URL] = []

        switch opts.fileLayout {
        case .perClass:
            var packagesTouched = Swift.Set<URL>()
            for cls in doc.classes {
                let module = emitter.module(for: cls)
                let code = generatePythonCode(from: module)
                let pkgParts = packageParts(of: cls.fqcn)
                var dir = opts.outputDir
                for part in pkgParts {
                    dir.appendPathComponent(part)
                    packagesTouched.insert(dir)
                }
                try FileManager.default.createDirectory(at: dir, withIntermediateDirectories: true)
                let file = dir.appendingPathComponent("\(cls.simpleName).py")
                try code.write(to: file, atomically: true, encoding: .utf8)
                written.append(file)
            }
            // Ensure every package on the path has an __init__.py
            for dir in packagesTouched {
                let initFile = dir.appendingPathComponent("__init__.py")
                if !FileManager.default.fileExists(atPath: initFile.path) {
                    try "".write(to: initFile, atomically: true, encoding: .utf8)
                    written.append(initFile)
                }
            }

        case .singleFile:
            var body: [Statement] = [.importFrom(.init(
                module: "jnius",
                names: [
                    Alias(name: "JavaClass", asName: nil),
                    Alias(name: "JavaInterface", asName: nil),
                    Alias(name: "MetaJavaClass", asName: nil),
                    Alias(name: "JavaMethod", asName: nil),
                    Alias(name: "JavaStaticMethod", asName: nil),
                    Alias(name: "JavaMultipleMethod", asName: nil),
                    Alias(name: "JavaField", asName: nil),
                    Alias(name: "JavaStaticField", asName: nil),
                ],
                level: 0
            ))]
            for cls in doc.classes {
                body.append(.blank(.init(count: 1)))
                body.append(.classDef(emitter.classDef(for: cls)))
            }
            let code = generatePythonCode(from: .module(body))
            let file = opts.outputDir.appendingPathComponent("wrappers.py")
            try code.write(to: file, atomically: true, encoding: .utf8)
            written.append(file)
        }
        return written
    }

    private func packageParts(of fqcn: String) -> [String] {
        let parts = fqcn.split(separator: ".").map(String.init)
        if parts.count <= 1 { return [] }
        return Array(parts.dropLast())
    }

    private func invokeJar(opts: Options) throws -> Data {
        let process = Process()
        process.executableURL = URL(fileURLWithPath: "/usr/bin/env")
        process.arguments = [
            opts.javaExecutable,
            "-jar", opts.jarPath.path,
            opts.inputDir.path,
        ]
        let stdoutPipe = Pipe()
        let stderrPipe = Pipe()
        process.standardOutput = stdoutPipe
        process.standardError = stderrPipe
        try process.run()
        // Drain pipes concurrently to avoid blocking the child on a full pipe
        // buffer (macOS default is ~64KB; large ASTs easily exceed this).
        var stdout = Data()
        var stderr = Data()
        let group = DispatchGroup()
        let queue = DispatchQueue(label: "pyjnius-wrap.pipe-drain", attributes: .concurrent)
        group.enter()
        queue.async {
            stdout = stdoutPipe.fileHandleForReading.readDataToEndOfFile()
            group.leave()
        }
        group.enter()
        queue.async {
            stderr = stderrPipe.fileHandleForReading.readDataToEndOfFile()
            group.leave()
        }
        process.waitUntilExit()
        group.wait()
        if process.terminationStatus != 0 {
            throw PipelineError.javaFailed(
                exitCode: process.terminationStatus,
                stderr: String(data: stderr, encoding: .utf8) ?? ""
            )
        }
        return stdout
    }
}
