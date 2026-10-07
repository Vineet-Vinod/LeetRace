import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: list[str] = []
    seen: set[tuple[tuple[int, int], ...]] = set()

    def add(peaks: list[list[int]]) -> None:
        key = tuple(map(tuple, peaks))
        if key not in seen:
            assert 1 <= len(peaks) <= 100_000
            assert all(
                len(peak) == 2 and 1 <= peak[0] <= 100_000 and 1 <= peak[1] <= 100_000
                for peak in peaks
            )
            seen.add(key)
            cases.append(f"candidate(peaks={peaks!r})")

    add([[2, 2], [6, 3], [5, 4]])
    add([[1, 3], [1, 3]])
    add([[10, 1], [10, 1], [10, 1]])
    add([[50_000, 1]] * 100_000)
    for _ in range(600):
        peaks = [
            [rng.randint(1, 100_000), rng.randint(1, 100_000)]
            for _ in range(rng.randint(1, 30))
        ]
        add(peaks)
    return cases
