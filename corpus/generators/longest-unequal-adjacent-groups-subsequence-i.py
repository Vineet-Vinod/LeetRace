def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {(("e", "a", "b"), (0, 0, 1)), (("a", "b", "c"), (0, 1, 0))}
    while len(cases) < 600:
        n = rng.randint(1, 50)
        unique_words = set()
        while len(unique_words) < n:
            unique_words.add(
                "".join(rng.choice("abcxyz") for _ in range(rng.randint(1, 10)))
            )
        words = tuple(sorted(unique_words))
        groups = tuple(rng.randrange(2) for _ in range(n))
        cases.add((words, groups))
    cases.add(
        (
            tuple(chr(97 + i // 26) + chr(97 + i % 26) for i in range(100)),
            tuple(i % 2 for i in range(100)),
        )
    )
    return [
        f"candidate(words={list(w)!r}, groups={list(g)!r})" for w, g in sorted(cases)
    ]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(words=['e', 'a', 'b'], groups=[0, 0, 1])",
    "candidate(words=['a', 'b', 'c', 'd'], groups=[1, 0, 1, 1])",
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
