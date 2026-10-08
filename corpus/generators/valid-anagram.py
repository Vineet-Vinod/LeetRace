def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    pairs = {
        ("anagram", "nagaram"),
        ("rat", "car"),
        ("a", "a"),
        ("ab", "a"),
        ("a" * 50000, "a" * 50000),
    }
    while len(pairs) < 600:
        n = rng.randint(1, 100)
        first = "".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(n))
        second = list(first)
        if rng.random() < 0.5:
            rng.shuffle(second)
        else:
            second[rng.randrange(n)] = rng.choice("abcdefghijklmnopqrstuvwxyz")
        pairs.add((first, "".join(second)))
    return [f"candidate(s={a!r}, t={b!r})" for a, b in sorted(pairs)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(s='anagram', t='nagaram')",
    "candidate(s='rat', t='car')",
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
