def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(2, 40)
        values = list(range(1, n + 1))
        rng.shuffle(values)
        descriptions = []
        available = [(values[0], 1), (values[0], 0)]
        for child in values[1:]:
            slot = rng.randrange(len(available))
            parent, is_left = available.pop(slot)
            descriptions.append([parent, child, is_left])
            available.append((child, 1))
            available.append((child, 0))
        cases.add(f"candidate(descriptions={descriptions!r})")
    return sorted(cases)
