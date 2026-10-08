def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(data=[1, 0, 1, 0, 1])", "candidate(data=[0, 0, 0, 1, 0])"])
    for index in range(600):
        size = 100000 if index == 0 else 1 + index % 1000
        data = [rng.randrange(2) for _ in range(size)]
        cases.add(f"candidate(data={data!r})")
    return sorted(cases)
