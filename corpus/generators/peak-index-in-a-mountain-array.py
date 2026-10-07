import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {
        (0, 1, 0),
        (0, 2, 1, 0),
        (0, 10, 5, 2),
        (0, 2, 4, 3, 1),
        (999_998, 1_000_000, 999_999),
    }
    cases.add(tuple(range(49_999)) + tuple(range(49_999, -1, -1)))
    while len(cases) < 600:
        left_size, right_size = rng.randint(1, 40), rng.randint(1, 40)
        peak = rng.randint(1000, 1_000_000)
        reverse_left = []
        value = peak
        for _ in range(left_size):
            value -= rng.randint(1, 10)
            reverse_left.append(value)
        left = list(reversed(reverse_left))
        right = []
        value = peak
        for _ in range(right_size):
            value -= rng.randint(1, 10)
            right.append(value)
        arr = tuple(left + [peak] + right)
        if min(arr) >= 0:
            cases.add(arr)
    assert all(
        3 <= len(arr) <= 100_000
        and 0 <= min(arr)
        and max(arr) <= 1_000_000
        and all(arr[index] < arr[index + 1] for index in range(arr.index(max(arr))))
        and all(
            arr[index] > arr[index + 1]
            for index in range(arr.index(max(arr)), len(arr) - 1)
        )
        for arr in cases
    )
    return [f"candidate(arr={list(arr)!r})" for arr in sorted(cases)]
