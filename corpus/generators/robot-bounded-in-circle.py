def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(instructions='GGLLGG')"}
    while len(cases) < 600:
        n = rng.randint(1, 100)
        instructions = "".join(rng.choice("GLR") for _ in range(n))
        cases.add(f"candidate(instructions={instructions!r})")
    return sorted(cases)
