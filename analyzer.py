import ast

def analyze_code(filepath):
    with open(filepath, "r") as f:
        tree = ast.parse(f.read())

    metrics = {
        "functions": 0,
        "avg_function_length": 0,
        "max_nesting_depth": 0,
        "list_comprehensions": 0,
        "classes": 0,
        "variable_name_lengths": []
    }

    function_lengths = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            metrics["functions"] += 1
            function_lengths.append(len(node.body))

        if isinstance(node, ast.ClassDef):
            metrics["classes"] += 1

        if isinstance(node, ast.ListComp):
            metrics["list_comprehensions"] += 1

        if isinstance(node, ast.Name):
            metrics["variable_name_lengths"].append(len(node.id))

    if function_lengths:
        metrics["avg_function_length"] = sum(function_lengths) / len(function_lengths)

    return metrics
