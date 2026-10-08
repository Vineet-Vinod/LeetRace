import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        shared = set(rng.sample(range(1, 2001), rng.randint(0, 30)))
        arrays = []
        for _ in range(3):
            values = shared | set(rng.sample(range(1, 2001), rng.randint(1, 100)))
            arrays.append(sorted(values))
        if not all(arrays):
            continue
        arr1, arr2, arr3 = arrays
        calls.add(f"candidate(arr1={arr1!r}, arr2={arr2!r}, arr3={arr3!r})")
    return sorted(calls)
