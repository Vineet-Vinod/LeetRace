def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:

        def intervals():
            result = []
            x = rng.randint(0, 10)
            for _ in range(rng.randint(0, 30)):
                start = x + rng.randint(0, 4)
                end = start + rng.randint(1, 100)
                result.append([start, end])
                x = end + rng.randint(1, 10)
            return result

        a, b = intervals(), intervals()
        if not a and not b:
            b = [[0, 1]]
        cases.add(f"candidate(firstList={a!r}, secondList={b!r})")
    return sorted(cases)
