import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        a = [rng.randint(1, 2000) for _ in range(rng.randint(1, 50))]
        b = [rng.randint(1, 2000) for _ in range(rng.randint(1, 50))]
        key = (tuple(a), tuple(b))
        if key not in seen:
            seen.add(key)
            assert a and b and all(1 <= v <= 2000 for v in a + b)
            cases.append(f"candidate(nums1={a!r}, nums2={b!r})")
    return cases
