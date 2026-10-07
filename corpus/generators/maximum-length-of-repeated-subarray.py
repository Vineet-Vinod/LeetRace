import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], tuple[int, ...]]] = {
        ((1, 2, 3, 2, 1), (3, 2, 1, 4, 7)),
        ((0, 0, 0, 0, 0), (0, 0, 0, 0, 0)),
        ((1,), (2,)),
        ((7,) * 1000, (7,) * 1000),
        ((0,) * 1000, (1,) * 1000),
    }
    while len(cases) < 600:
        mode = rng.randrange(4)
        if mode == 0:
            size1, size2 = rng.randint(1, 100), rng.randint(1, 100)
            common = tuple(
                rng.randint(0, 100) for _ in range(rng.randint(1, min(size1, size2)))
            )
            first = (
                tuple(rng.randint(0, 100) for _ in range(size1 - len(common))) + common
            )
            second = common + tuple(
                rng.randint(0, 100) for _ in range(size2 - len(common))
            )
        elif mode == 1:
            first = tuple(rng.randint(0, 49) for _ in range(rng.randint(1, 100)))
            second = tuple(rng.randint(50, 100) for _ in range(rng.randint(1, 100)))
        elif mode == 2:
            first = tuple(rng.randint(0, 100) for _ in range(rng.randint(1, 100)))
            second = tuple(reversed(first))
        else:
            first = tuple(rng.randint(0, 100) for _ in range(rng.randint(1, 100)))
            second = tuple(rng.randint(0, 100) for _ in range(rng.randint(1, 100)))
        cases.add((first, second))
    assert all(
        1 <= len(first) <= 1000
        and 1 <= len(second) <= 1000
        and all(0 <= value <= 100 for value in first + second)
        for first, second in cases
    )
    return [
        f"candidate(nums1={list(first)!r}, nums2={list(second)!r})"
        for first, second in sorted(cases)
    ]
