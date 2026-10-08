def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        ("cba", "daf", "ghi"),
        ("a", "b"),
        ("zyx", "wvu", "tsr"),
        ("abc", "bce"),
        tuple("a" * 100 for _ in range(100)),
    }
    while len(cases) < 600:
        rows, cols = rng.randint(1, 20), rng.randint(1, 20)
        cases.add(
            tuple(
                "".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(cols))
                for _ in range(rows)
            )
        )
    return [f"candidate(strs={list(rows)!r})" for rows in sorted(cases)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(strs=['cba', 'daf', 'ghi'])",
    "candidate(strs=['a', 'b'])",
    "candidate(strs=['zyx', 'wvu', 'tsr'])",
]
_ORIGINAL_GENERATE = generate


def generate(seed: int = 0) -> list[str]:
    import ast

    calls = _ORIGINAL_GENERATE(seed) + _STATEMENT_EXAMPLE_CALLS
    unique = {}
    for call in calls:
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        unique.setdefault(key, call)
    return [unique[key] for key in sorted(unique)]
