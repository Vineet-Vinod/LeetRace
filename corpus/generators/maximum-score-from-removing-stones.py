def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(a=2, b=4, c=6)", "candidate(a=4, b=4, c=6)"])
    for index in range(600):
        values = [rng.randint(1, 100000) for _ in range(3)]
        cases.add(f"candidate(a={values[0]}, b={values[1]}, c={values[2]})")
    while len(cases) < 600:
        values = [rng.randint(1, 100000) for _ in range(3)]
        cases.add(f"candidate(a={values[0]}, b={values[1]}, c={values[2]})")
    return sorted(cases)
