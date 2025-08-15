import ast

def find_imports(filename):
    with open(filename, "r") as file:
        tree = ast.parse(file.read(), filename)

    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module)
            for alias in node.names:
                imports.add(f"{node.module}.{alias.name}" if node.module else alias.name)
    
    return imports

if __name__ == "__main__":
    filename = "app.py"
    imports = find_imports(filename)
    print("Modules used in {}:".format(filename))
    for module in imports:
        print(module)
