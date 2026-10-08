def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    cases.update(
        ["candidate(s='(123)')", "candidate(s='(0123)')", "candidate(s='(00011)')"]
    )
    while len(cases) < 600:
        n = rng.randint(2, 10)
        digits = "".join(rng.choice("0123456789") for _ in range(n))
        cases.add(f"candidate(s={('(' + digits + ')')!r})")
    return sorted(cases)
