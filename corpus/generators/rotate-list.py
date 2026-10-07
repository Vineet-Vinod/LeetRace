import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        values = [rng.randint(-100, 100) for _ in range(rng.randint(0, 80))]
        k = rng.randint(0, 2 * 10**9)
        key = (tuple(values), k)
        if key not in seen:
            seen.add(key)
            assert (
                len(values) <= 500
                and 0 <= k <= 2 * 10**9
                and all(-100 <= v <= 100 for v in values)
            )
            cases.append(f"candidate(head=list_node({values!r}), k={k})")
    return cases
