def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(spells=[5,1,3],potions=[1,2,3,4,5],success=7)"}
    while len(cases) < 600:
        spells = [rng.randint(1, 10**5) for _ in range(rng.randint(1, 40))]
        potions = [rng.randint(1, 10**5) for _ in range(rng.randint(1, 40))]
        success = rng.randint(1, 10**10)
        cases.add(f"candidate(spells={spells!r},potions={potions!r},success={success})")
    return sorted(cases)
