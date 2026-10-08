import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: equal arrays length1..2*10^4; apples/days0..2*10^4 and both zero exactly together; includes n=20000 case."""
    rng = random.Random(seed)
    calls = {
        "candidate(apples=[1, 2, 3, 5, 2], days=[3, 2, 1, 4, 2])",
        "candidate(apples=[3, 0, 0, 0, 0, 2], days=[3, 0, 0, 0, 0, 2])",
        f"candidate(apples={[1] * 20000!r}, days={[1] * 20000!r})",
    }
    while len(calls) < 600:
        size = rng.randint(1, 100)
        apples = [rng.randint(0, 100) for _ in range(size)]
        days = [rng.randint(1, 100) if count else 0 for count in apples]
        calls.add(f"candidate(apples={apples!r}, days={days!r})")
    return sorted(calls)
