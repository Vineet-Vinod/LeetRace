import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(2, 4, 2, 3), (1, 100_000), (5, 4), (1, 1)}
    cases.add(tuple([1] * 100_000))
    while len(cases) < 600:
        size = rng.randrange(1, 51) * 2
        cases.add(tuple(rng.randint(1, 100_000) for _ in range(size)))
    assert all(
        2 <= len(values) <= 100_000
        and len(values) % 2 == 0
        and all(1 <= value <= 100_000 for value in values)
        for values in cases
    )
    return [f"candidate(head=list_node({list(values)!r}))" for values in sorted(cases)]
