import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], int]] = {
        ((3, 2, 2), 2),
        ((2,), 10),
        ((1,), 0),
        ((1, 10**9), 10**9),
    }
    cases.add((tuple([1] * 100_000), 10**9))
    while len(cases) < 600:
        energies = tuple(rng.randint(1, 10**9) for _ in range(rng.randint(1, 70)))
        cases.add((energies, rng.randint(0, 10**9)))
    assert all(
        1 <= len(energies) <= 100_000
        and 0 <= power <= 10**9
        and all(1 <= value <= 10**9 for value in energies)
        for energies, power in cases
    )
    return [
        f"candidate(enemyEnergies={list(energies)!r}, currentEnergy={power})"
        for energies, power in sorted(cases)
    ]
