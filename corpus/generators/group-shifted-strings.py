def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            'candidate(strings=["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])',
            "candidate(strings=[chr(97 + i % 26) * 50 for i in range(200)])",
        ]
    )
    for index in range(600):
        strings = []
        for _ in range(1 + index % 50):
            size = 1 + rng.randrange(50)
            strings.append(
                "".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(size))
            )
        cases.add(f"candidate(strings={strings!r})")
    while len(cases) < 600:
        strings = [
            "".join(
                rng.choice("abcdefghijklmnopqrstuvwxyz")
                for _ in range(rng.randint(1, 50))
            )
            for _ in range(rng.randint(1, 30))
        ]
        cases.add(f"candidate(strings={strings!r})")
    return sorted(cases)
