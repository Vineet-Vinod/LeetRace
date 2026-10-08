def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(arr=[4,9,3],target=10)"}
    while len(cases) < 600:
        arr = [rng.randint(1, 10**5) for _ in range(rng.randint(1, 50))]
        target = rng.randint(1, 10**5)
        cases.add(f"candidate(arr={arr!r},target={target})")
    return sorted(cases)
