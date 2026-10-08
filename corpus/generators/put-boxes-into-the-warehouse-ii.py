import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: list[str] = []
    seen: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()

    def add(boxes: list[int], warehouse: list[int]) -> None:
        key = (tuple(boxes), tuple(warehouse))
        if key not in seen:
            assert 1 <= len(boxes) <= 100_000 and 1 <= len(warehouse) <= 100_000
            assert all(1 <= height <= 10**9 for height in boxes + warehouse)
            seen.add(key)
            cases.append(f"candidate(boxes={boxes!r}, warehouse={warehouse!r})")

    add([1, 2, 2, 3, 4], [3, 4, 1, 2])
    add([3, 5, 5, 2], [2, 1, 3, 4, 5])
    add([10**9] * 100_000, [10**9] * 100_000)
    for _ in range(600):
        boxes = [rng.randint(1, 1000) for _ in range(rng.randint(1, 50))]
        warehouse = [rng.randint(1, 1000) for _ in range(rng.randint(1, 50))]
        add(boxes, warehouse)
    return cases
