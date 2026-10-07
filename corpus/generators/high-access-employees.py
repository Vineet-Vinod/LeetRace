def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        ['candidate(access_times=[["a", "0549"], ["a", "0532"], ["a", "0621"]])']
    )
    for index in range(600):
        count = 1 + index % 100
        entries = []
        for access_index in range(count):
            name = "e" + chr(97 + access_index % max(1, min(26, count)))
            minute = rng.randrange(24 * 60)
            entries.append([name, f"{minute // 60:02d}{minute % 60:02d}"])
        cases.add(f"candidate(access_times={entries!r})")
    while len(cases) < 600:
        entries = []
        for access_index in range(rng.randint(1, 100)):
            minute = rng.randrange(24 * 60)
            entries.append(
                [chr(97 + access_index % 26), f"{minute // 60:02d}{minute % 60:02d}"]
            )
        cases.add(f"candidate(access_times={entries!r})")
    return sorted(cases)
