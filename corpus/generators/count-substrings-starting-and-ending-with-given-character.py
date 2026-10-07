def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            'candidate(s="abada", c="a")',
            'candidate(s="zzz", c="z")',
            f"candidate(s={'a' * 100000!r}, c='a')",
        ]
    )
    for index in range(600):
        size = 1 + index % 200
        c = rng.choice("abcdefghijklmnopqrstuvwxyz")
        s = "".join(
            c if rng.randrange(4) == 0 else rng.choice("abcdefghijklmnopqrstuvwxyz")
            for _ in range(size)
        )
        cases.add(f"candidate(s={s!r}, c={c!r})")
    while len(cases) < 600:
        c = rng.choice("abcdefghijklmnopqrstuvwxyz")
        s = "".join(
            rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(rng.randint(1, 100))
        )
        cases.add(f"candidate(s={s!r}, c={c!r})")
    return sorted(cases)
