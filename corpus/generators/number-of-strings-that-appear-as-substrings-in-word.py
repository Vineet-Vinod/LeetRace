def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        (("a", "abc", "bc", "d"), "abc"),
        (("a", "a", "aa"), "aaaa"),
        (tuple("a" * 100 for _ in range(100)), "a" * 100),
    }
    while len(cases) < 600:
        word = "".join(rng.choice("abcxyz") for _ in range(rng.randint(1, 50)))
        patterns = tuple(
            "".join(rng.choice("abcxyz") for _ in range(rng.randint(1, 10)))
            for _ in range(rng.randint(1, 20))
        )
        cases.add((patterns, word))
    return [f"candidate(patterns={list(p)!r}, word={w!r})" for p, w in sorted(cases)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(patterns=['a', 'abc', 'bc', 'd'], word='abc')",
    "candidate(patterns=['a', 'b', 'c'], word='aaaaabbbbb')",
    "candidate(patterns=['a', 'a', 'a'], word='ab')",
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
