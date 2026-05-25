import Foundation

/// Emits a PEP-484 `.pyi` stub file with Pythonic types for each pyjnius
/// wrapper class. The intent is editor / type-checker friendliness:
/// `String` → `str`, `int`/`long`/`Integer` → `int`, `List` → `list`,
/// arrays → `list[T]`, varargs → `*name: T`, overloaded methods → `@overload`,
/// static fields → `ClassVar[T]`, enum constants → `ClassVar[Self]`.
///
/// Unknown reference types fall back to a quoted forward reference using
/// the simple class name.
public struct PyiStubEmitter {

    public init() {}

    /// Render a `.pyi` stub for a single top-level class (with nested types
    /// embedded as nested `class` blocks).
    public func render(_ cls: ClassNode) -> String {
        var lines: [String] = []
        lines.append("from typing import Any, ClassVar, overload")
        lines.append("")
        appendClass(cls, indent: "", into: &lines)
        return lines.joined(separator: "\n") + "\n"
    }

    // MARK: - Class

    private func appendClass(_ cls: ClassNode, indent: String, into lines: inout [String]) {
        lines.append("\(indent)class \(cls.simpleName):")
        let body = indent + "    "
        var produced = false

        // Enum constants
        if cls.kind == .enumType, let constants = cls.enumConstants {
            for ec in constants {
                lines.append("\(body)\(ec.name): ClassVar[\"\(cls.simpleName)\"]")
                produced = true
            }
        }

        // Static then instance fields
        for f in cls.fields where f.isStatic {
            lines.append("\(body)\(safeName(f.name)): ClassVar[\(pyType(of: f.typeFqcn))]")
            produced = true
        }
        for f in cls.fields where !f.isStatic {
            lines.append("\(body)\(safeName(f.name)): \(pyType(of: f.typeFqcn))")
            produced = true
        }

        // Constructors → __init__
        if cls.kind != .interfaceType && !cls.constructors.isEmpty {
            if cls.constructors.count == 1 {
                let c = cls.constructors[0]
                let params = formatParams(c.parameters, varargs: c.isVarargs, includeSelf: true)
                lines.append("\(body)def __init__\(params) -> None: ...")
            } else {
                for c in cls.constructors {
                    lines.append("\(body)@overload")
                    let params = formatParams(c.parameters, varargs: c.isVarargs, includeSelf: true)
                    lines.append("\(body)def __init__\(params) -> None: ...")
                }
            }
            produced = true
        }

        // Methods grouped by name (preserves declaration order)
        var order: [String] = []
        var bucket: [String: [MethodNode]] = [:]
        for m in cls.methods {
            if bucket[m.name] == nil { order.append(m.name) }
            bucket[m.name, default: []].append(m)
        }
        for name in order {
            let methods = bucket[name]!
            let safe = safeName(name)
            if methods.count == 1 {
                emitMethod(methods[0], pyName: safe, body: body, overload: false, into: &lines)
            } else {
                for m in methods {
                    emitMethod(m, pyName: safe, body: body, overload: true, into: &lines)
                }
            }
            produced = true
        }

        // Nested classes
        for n in cls.nested {
            lines.append("")
            appendClass(n, indent: body, into: &lines)
            produced = true
        }

        if !produced {
            lines.append("\(body)...")
        }
    }

    private func emitMethod(_ m: MethodNode, pyName: String, body: String,
                            overload: Bool, into lines: inout [String]) {
        if overload { lines.append("\(body)@overload") }
        if m.isStatic { lines.append("\(body)@staticmethod") }
        let params = formatParams(m.parameters, varargs: m.isVarargs, includeSelf: !m.isStatic)
        let ret = pyType(of: m.returnTypeFqcn)
        lines.append("\(body)def \(pyName)\(params) -> \(ret): ...")
    }

    // MARK: - Params

    private func formatParams(_ params: [ParamNode], varargs: Bool, includeSelf: Bool) -> String {
        var parts: [String] = []
        if includeSelf { parts.append("self") }
        let last = params.count - 1
        for (i, p) in params.enumerated() {
            let name = safeParamName(p.name, idx: i)
            if varargs && i == last && p.typeFqcn.hasSuffix("[]") {
                let inner = pyType(of: String(p.typeFqcn.dropLast(2)))
                parts.append("*\(name): \(inner)")
            } else {
                parts.append("\(name): \(pyType(of: p.typeFqcn))")
            }
        }
        return "(" + parts.joined(separator: ", ") + ")"
    }

    private func safeParamName(_ name: String, idx: Int) -> String {
        let n = name.isEmpty ? "arg\(idx)" : name
        return safeName(n)
    }

    private func safeName(_ s: String) -> String {
        Self.pyKeywords.contains(s) ? s + "_" : s
    }

    private static let pyKeywords: Swift.Set<String> = [
        "False","None","True","and","as","assert","async","await","break","class",
        "continue","def","del","elif","else","except","finally","for","from","global",
        "if","import","in","is","lambda","nonlocal","not","or","pass","raise","return",
        "try","while","with","yield","match","case"
    ]

    // MARK: - Type mapping

    /// Java FQCN (or "int[]"-style array string) → Python annotation.
    public func pyType(of fqcn: String) -> String {
        if fqcn.hasSuffix("[]") {
            return "list[\(pyType(of: String(fqcn.dropLast(2))))]"
        }
        switch fqcn {
        case "void": return "None"
        case "boolean": return "bool"
        case "byte", "short", "int", "long": return "int"
        case "float", "double": return "float"
        case "char": return "str"
        case "java.lang.String", "java.lang.CharSequence": return "str"
        case "java.lang.Object": return "Any"
        case "java.lang.Boolean": return "bool"
        case "java.lang.Integer", "java.lang.Long",
             "java.lang.Short", "java.lang.Byte": return "int"
        case "java.lang.Float", "java.lang.Double", "java.lang.Number": return "float"
        case "java.lang.Character": return "str"
        case "java.util.List", "java.util.Collection",
             "java.util.ArrayList", "java.util.LinkedList": return "list"
        case "java.util.Map", "java.util.HashMap", "java.util.LinkedHashMap",
             "java.util.TreeMap": return "dict"
        case "java.util.Set", "java.util.HashSet", "java.util.LinkedHashSet",
             "java.util.TreeSet": return "set"
        case "java.lang.Class": return "type"
        default:
            // Forward-reference by simple name. For nested types Java uses '.' in
            // typeFqcn, but pyjnius only knows the outermost class so the simple
            // name is the most useful hint for IDE autocomplete.
            let simple = fqcn.split(separator: ".").last.map(String.init) ?? fqcn
            return "\"\(simple)\""
        }
    }
}
