import ArgumentParser
import Foundation
import PyjniusWrapCore

@main
struct PyjniusWrap: ParsableCommand {
    static let configuration = CommandConfiguration(
        commandName: "pyjnius-wrap",
        abstract: "Generate pyjnius wrapper modules from Java sources."
    )

    @Argument(help: "Folder containing .java source files to scan recursively.")
    var inputDir: String

    @Argument(help: "Destination folder for generated Python files.")
    var outputDir: String

    @Option(name: .long, help: "Override the bundled java-ast-emitter.jar path.")
    var jar: String?

    @Option(name: .long, help: "Override the java executable.")
    var javaExecutable: String = "java"

    @Flag(name: .long, help: "Flatten output into a single wrappers.py file.")
    var singleFile: Bool = false

    @Flag(name: .long,
          help: "Keep the full Java reverse-DNS package path (e.g. com/google/android/gms/ads/MobileAds.py). Default: strip the longest common prefix for a shorter, more Pythonic layout.")
    var keepPackagePrefix: Bool = false

    func run() throws {
        let inURL = URL(fileURLWithPath: inputDir)
        let outURL = URL(fileURLWithPath: outputDir)
        let jarURL: URL
        if let jar { jarURL = URL(fileURLWithPath: jar) }
        else { jarURL = try resolveBundledJar() }

        let pipeline = Pipeline()
        let written = try pipeline.run(.init(
            inputDir: inURL,
            outputDir: outURL,
            jarPath: jarURL,
            javaExecutable: javaExecutable,
            fileLayout: singleFile ? .singleFile : .perClass,
            stripCommonPackagePrefix: !keepPackagePrefix
        ))
        for url in written {
            print(url.path)
        }
    }

    private func resolveBundledJar() throws -> URL {
        if let url = Bundle.module.url(forResource: "java-ast-emitter", withExtension: "jar") {
            return url
        }
        throw ValidationError("Bundled java-ast-emitter.jar not found; pass --jar explicitly.")
    }
}
