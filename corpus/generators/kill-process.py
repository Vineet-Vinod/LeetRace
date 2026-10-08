def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(pid=[1, 3, 10, 5], ppid=[3, 0, 5, 3], kill=5)"])
    for index in range(600):
        size = 1 + index % 200
        pid = list(range(1, size + 1))
        ppid = [0] + [rng.randint(1, value - 1) for value in range(2, size + 1)]
        kill = rng.randint(1, size)
        cases.add(f"candidate(pid={pid!r}, ppid={ppid!r}, kill={kill})")
    while len(cases) < 600:
        size = rng.randint(1, 200)
        pid = list(range(1, size + 1))
        ppid = [0] + [rng.randint(1, value - 1) for value in range(2, size + 1)]
        cases.add(f"candidate(pid={pid!r}, ppid={ppid!r}, kill={rng.randint(1, size)})")
    return sorted(cases)
