def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {("02:30", "04:35"), ("11:00", "11:01"), ("00:00", "23:59")}
    while len(cases) < 600:
        a = rng.randint(0, 1438)
        b = rng.randint(a, 1439)
        cases.add((f"{a // 60:02d}:{a % 60:02d}", f"{b // 60:02d}:{b % 60:02d}"))
    return [f"candidate(current={a!r}, correct={b!r})" for a, b in sorted(cases)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(current='02:30', correct='04:35')",
    "candidate(current='11:00', correct='11:01')",
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
