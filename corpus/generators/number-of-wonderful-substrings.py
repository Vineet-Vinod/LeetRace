def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(['candidate(word="aba")', 'candidate(word="aabb")'])
    for index in range(600):
        size = 100000 if index == 0 else 1 + index % 1000
        word = "".join(rng.choice("abcdefghij") for _ in range(size))
        cases.add(f"candidate(word={word!r})")
    return sorted(cases)
