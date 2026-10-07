import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        n = rng.randint(1, 80)
        alice = [rng.randint(1, 100) for _ in range(n)]
        bob = [rng.randint(1, 100) for _ in range(n)]
        key = (tuple(alice), tuple(bob))
        if key not in seen:
            seen.add(key)
            assert len(alice) == len(bob) and all(1 <= v <= 100 for v in alice + bob)
            cases.append(f"candidate(aliceValues={alice!r}, bobValues={bob!r})")
    return cases
