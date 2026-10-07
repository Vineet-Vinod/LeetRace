import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        arr = [rng.randint(-100000, 100000) for _ in range(rng.randint(1, 80))]
        k = rng.randint(1, len(arr))
        key = (tuple(arr), k)
        if key not in seen:
            seen.add(key)
            assert (
                arr and 1 <= k <= len(arr) and all(-(10**5) <= v <= 10**5 for v in arr)
            )
            cases.append(f"candidate(arr={arr!r}, k={k})")
    return cases
