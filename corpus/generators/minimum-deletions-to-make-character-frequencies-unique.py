def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            'candidate(s="aab")',
            'candidate(s="aaabbbcc")',
            f"candidate(s={'a' * 100000!r})",
        ]
    )
    for index in range(600):
        size = 1 + index % 1000
        s = "".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(size))
        if index % 4 == 0:
            s = "a" * size
        cases.add(f"candidate(s={s!r})")
    return sorted(cases)
