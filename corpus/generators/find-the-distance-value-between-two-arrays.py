import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        arr1 = [rng.randint(-1000, 1000) for _ in range(rng.randint(1, 500))]
        arr2 = [rng.randint(-1000, 1000) for _ in range(rng.randint(1, 500))]
        d = rng.randint(0, 100)
        calls.add(f"candidate(arr1={arr1!r}, arr2={arr2!r}, d={d})")
    return sorted(calls)
