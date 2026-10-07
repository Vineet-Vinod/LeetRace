def generate(seed: int = 0) -> list[str]:
    # The legal input domain is exactly n in [1, 200], so enumerate all 200.
    return [f"candidate(n={n})" for n in range(1, 201)]


DOMAIN_SIZE = 200

_STATEMENT_EXAMPLE_CALLS = ["candidate(n=7)", "candidate(n=14)"]
_ORIGINAL_GENERATE = generate


def generate(seed: int = 0) -> list[str]:
    import ast

    calls = _ORIGINAL_GENERATE(seed) + _STATEMENT_EXAMPLE_CALLS
    unique = {}
    for call in calls:
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        unique.setdefault(key, call)
    return [unique[key] for key in sorted(unique)]
