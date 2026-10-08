import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        arr = [rng.randint(1, 10000) for _ in range(rng.randint(1, 80))]
        k = rng.randint(1, len(arr))
        threshold = rng.randint(0, 10000)
        key = (tuple(arr), k, threshold)
        if key not in seen:
            seen.add(key)
            assert (
                1 <= k <= len(arr)
                and all(1 <= v <= 10000 for v in arr)
                and 0 <= threshold <= 10000
            )
            cases.append(f"candidate(arr={arr!r}, k={k}, threshold={threshold})")
    return cases
