def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(dominoes='RR.L')",
        "candidate(dominoes='.L.R...LR..L..')",
        f"candidate(dominoes={'R' + '.' * 99_998 + 'L'!r})",
    }
    while len(cases) < 600:
        n = rng.randint(1, 1000)
        dominoes = "".join(rng.choice("LR.") for _ in range(n))
        assert 1 <= len(dominoes) <= 100_000 and set(dominoes) <= set("LR.")
        cases.add(f"candidate(dominoes={dominoes!r})")
    return sorted(cases)
