def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            'candidate(strs=["ca", "bb", "ac"])',
            'candidate(strs=["xc", "yb", "za"])',
            "candidate(strs=[chr(97 + i % 26) * 100 for i in range(100)])",
        ]
    )
    for index in range(600):
        rows, width = 1 + index % 20, 1 + (index * 7) % 20
        strs = [
            "".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(width))
            for _ in range(rows)
        ]
        if index % 3 == 0:
            strs.sort()
        cases.add(f"candidate(strs={strs!r})")
    while len(cases) < 600:
        rows, width = rng.randint(1, 20), rng.randint(1, 20)
        strs = [
            "".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(width))
            for _ in range(rows)
        ]
        cases.add(f"candidate(strs={strs!r})")
    return sorted(cases)
