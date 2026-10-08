import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = {
        "candidate(list_node([-10, -3, 0, 5, 9]))",
        "candidate(list_node([]))",
    }
    while len(calls) < 600:
        size = rng.randint(0, 100)
        start = rng.randint(-100000, 100000 - size)
        values = list(range(start, start + size))
        calls.add(f"candidate(list_node({values!r}))")
    return sorted(calls)
