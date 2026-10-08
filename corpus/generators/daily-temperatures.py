def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(temperatures=[73, 74, 75, 71, 69, 72, 76, 73])"])
    for index in range(600):
        size = 100000 if index % 250 == 0 else 1 + index % 100
        temperatures = [rng.randint(30, 100) for _ in range(size)]
        if index % 4 == 0:
            temperatures.sort()
        elif index % 4 == 1:
            temperatures.sort(reverse=True)
        cases.add(f"candidate(temperatures={temperatures!r})")
    while len(cases) < 600:
        temperatures = [rng.randint(30, 100) for _ in range(rng.randint(1, 50))]
        cases.add(f"candidate(temperatures={temperatures!r})")
    return sorted(cases)
