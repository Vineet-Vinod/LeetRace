import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        n = rng.randint(2, 80)
        skills = rng.sample(range(1, 10**6 + 1), n)
        k = rng.randint(1, 10**9)
        key = (tuple(skills), k)
        if key not in seen:
            seen.add(key)
            assert (
                len(skills) == n
                and len(set(skills)) == n
                and all(1 <= v <= 10**6 for v in skills)
            )
            cases.append(f"candidate(skills={skills!r}, k={k})")
    return cases
