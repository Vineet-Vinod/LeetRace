def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {("abcdefghi", 3, "x"), ("abcdefghij", 3, "z"), ("a", 1, "b")}
    while len(cases) < 600:
        n, k = rng.randint(1, 100), rng.randint(1, 100)
        cases.add(
            (
                "".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(n)),
                k,
                rng.choice("abcdefghijklmnopqrstuvwxyz"),
            )
        )
    return [f"candidate(s={s!r}, k={k}, fill={fill!r})" for s, k, fill in sorted(cases)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(s='abcdefghi', k=3, fill='x')",
    "candidate(s='abcdefghij', k=3, fill='x')",
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
