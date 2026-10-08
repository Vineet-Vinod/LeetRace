import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        values = [rng.randint(0, 100) for _ in range(rng.randint(0, 100))]
        key = tuple(values)
        if key not in seen:
            seen.add(key)
            assert len(values) <= 100 and all(0 <= v <= 100 for v in values)
            cases.append(f"candidate(head=list_node({values!r}))")
    return cases
