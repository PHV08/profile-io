def generate_profile(metrics):
    profile = {}

    if metrics["avg_function_length"] > 20:
        profile["Function Style"] = "Monolithic thinker"
    else:
        profile["Function Style"] = "Modular builder"

    if metrics["classes"] > metrics["functions"]:
        profile["Paradigm Bias"] = "OOP-leaning"
    else:
        profile["Paradigm Bias"] = "Functional-leaning"

    avg_var_length = (
        sum(metrics["variable_name_lengths"]) /
        len(metrics["variable_name_lengths"])
        if metrics["variable_name_lengths"] else 0
    )

    profile["Variable Naming"] = (
        "Verbose and expressive"
        if avg_var_length > 8 else
        "Concise and minimal"
    )

    profile["List Comprehension Usage"] = metrics["list_comprehensions"]

    return profile
