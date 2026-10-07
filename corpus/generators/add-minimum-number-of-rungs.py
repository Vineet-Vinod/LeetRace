import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        n = rng.randint(1, 30)
        dist = rng.randint(1, 20)
        rungs = sorted(rng.sample(range(1, 1000), n))
        key = (tuple(rungs), dist)
        if key not in seen:
            seen.add(key)
            assert all(a < b for a, b in zip(rungs, rungs[1:]))
            cases.append(f"candidate(rungs={rungs!r}, dist={dist})")
    cases.extend(
        [
            "candidate(rungs=[1], dist=1)",
            "candidate(rungs=[1000000000], dist=1000000000)",
        ]
    )
    return cases[:600]
