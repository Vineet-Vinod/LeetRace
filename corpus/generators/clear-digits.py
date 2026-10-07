def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    strings = {"abc", "cb34", "a1b2c3", "leet2code3", "a1" * 50}
    alphabet = "abcxyz"
    while len(strings) < 600:
        out = []
        letters = 0
        for _ in range(rng.randint(1, 40)):
            if letters and rng.random() < 0.25:
                out.append(rng.choice("0123456789"))
                letters -= 1
            else:
                out.append(rng.choice(alphabet))
                letters += 1
        strings.add("".join(out))
    return [f"candidate(s={s!r})" for s in sorted(strings)]


_STATEMENT_EXAMPLE_CALLS = ["candidate(s='abc')", "candidate(s='cb34')"]
_ORIGINAL_GENERATE = generate


def generate(seed: int = 0) -> list[str]:
    import ast

    calls = _ORIGINAL_GENERATE(seed) + _STATEMENT_EXAMPLE_CALLS
    unique = {}
    for call in calls:
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        unique.setdefault(key, call)
    return [unique[key] for key in sorted(unique)]
