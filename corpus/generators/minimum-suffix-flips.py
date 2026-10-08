def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(target='0')", "candidate(target='10111')"}
    while len(cases) < 600:
        n = rng.randint(1, 500)
        target = "".join(rng.choice("01") for _ in range(n))
        cases.add(f"candidate(target={target!r})")
    return sorted(cases)
