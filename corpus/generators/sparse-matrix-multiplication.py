import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        m = rng.randint(1, 12)
        k = rng.randint(1, 12)
        n = rng.randint(1, 12)
        mat1 = [
            [rng.randint(-100, 100) if rng.random() < 0.2 else 0 for _ in range(k)]
            for _ in range(m)
        ]
        mat2 = [
            [rng.randint(-100, 100) if rng.random() < 0.2 else 0 for _ in range(n)]
            for _ in range(k)
        ]
        key = (tuple(map(tuple, mat1)), tuple(map(tuple, mat2)))
        if key not in seen:
            seen.add(key)
            assert (
                len(mat1) == m
                and all(len(r) == k for r in mat1)
                and len(mat2) == k
                and all(len(r) == n for r in mat2)
            )
            cases.append(f"candidate(mat1={mat1!r}, mat2={mat2!r})")
    return cases
