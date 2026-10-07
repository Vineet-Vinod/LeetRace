import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[tuple[int, int, int], ...], tuple[int, int, int]]] = {
        (((2, 5, 3), (1, 8, 4), (1, 7, 5)), (2, 7, 5)),
        (((3, 4, 5), (4, 5, 6)), (3, 2, 5)),
        (((2, 5, 3), (2, 3, 4), (1, 2, 5), (5, 2, 3)), (5, 5, 5)),
        (((1, 1, 1),) * 100_000, (1, 1, 1)),
        (((1000, 1, 1), (1, 1000, 1), (1, 1, 1000)), (1000, 1000, 1000)),
    }
    while len(cases) < 600:
        target = tuple(rng.randint(1, 1000) for _ in range(3))
        size = rng.randint(1, 30)
        if rng.random() < 0.65:
            triplets = [
                tuple(
                    target[index] if j == index else rng.randint(1, target[j])
                    for j in range(3)
                )
                for index in range(3)
            ]
            triplets.extend(
                tuple(rng.randint(1, target[j]) for j in range(3))
                for _ in range(size - 3)
            )
        else:
            triplets = [
                tuple(rng.randint(1, 1000) for _ in range(3)) for _ in range(size)
            ]
        cases.add((tuple(triplets), target))
    assert all(
        1 <= len(triplets) <= 100_000
        and all(
            len(triplet) == 3 and all(1 <= value <= 1000 for value in triplet)
            for triplet in triplets
        )
        and all(1 <= value <= 1000 for value in target)
        for triplets, target in cases
    )
    return [
        f"candidate(triplets={[list(t) for t in triplets]!r}, target={list(target)!r})"
        for triplets, target in sorted(cases)
    ]
