import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {((1, 2), (2, 3), (3, 4)), ((1, 2), (2, 3), (3, 4), (1, 2))}
    while len(cases) < 600:
        events = tuple(
            (start := rng.randint(1, 100), rng.randint(start, 120))
            for _ in range(rng.randint(1, 80))
        )
        cases.add(events)
    return [
        f"candidate(events={[list(event) for event in events]!r})" for events in cases
    ]
