import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: n1..25, k0..100, valid start cell."""
    rng = random.Random(seed)
    calls = {
        "candidate(n=3, k=2, row=0, column=0)",
        "candidate(n=1, k=0, row=0, column=0)",
    }
    while len(calls) < 600:
        n = rng.randint(1, 25)
        k = rng.randint(0, 100)
        row, column = rng.randrange(n), rng.randrange(n)
        calls.add(f"candidate(n={n}, k={k}, row={row}, column={column})")
    return sorted(calls)
