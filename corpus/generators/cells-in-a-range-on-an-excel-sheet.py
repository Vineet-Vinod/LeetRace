def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    ranges = {"K1:L2", "A1:B1", "A1:A9", "Y8:Z9", "C3:F4", "A1:Z9"}
    while len(ranges) < 600:
        c1 = rng.randrange(26)
        c2 = rng.randrange(c1, 26)
        r1 = rng.randint(1, 9)
        r2 = rng.randint(r1, 9)
        ranges.add(f"{chr(65 + c1)}{r1}:{chr(65 + c2)}{r2}")
    return [f"candidate(s={s!r})" for s in sorted(ranges)]


_STATEMENT_EXAMPLE_CALLS = ["candidate(s='K1:L2')", "candidate(s='A1:F1')"]
_ORIGINAL_GENERATE = generate


def generate(seed: int = 0) -> list[str]:
    import ast

    calls = _ORIGINAL_GENERATE(seed) + _STATEMENT_EXAMPLE_CALLS
    unique = {}
    for call in calls:
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        unique.setdefault(key, call)
    return [unique[key] for key in sorted(unique)]
