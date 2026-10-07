def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    strings = {"a0b1c2", "leetcode", "1229857369", "covid2019", "a" * 250 + "0" * 250}
    while len(strings) < 600:
        n = rng.randint(1, 100)
        chars = [rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(n)]
        for i in range(rng.randint(0, n)):
            chars[rng.randrange(n)] = rng.choice("0123456789")
        strings.add("".join(chars))
    return [f"candidate(s={s!r})" for s in sorted(strings)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(s='a0b1c2')",
    "candidate(s='leetcode')",
    "candidate(s='1229857369')",
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
