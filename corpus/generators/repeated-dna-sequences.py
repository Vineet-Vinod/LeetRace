def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(s='AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')",
        "candidate(s='AAAAAAAAAAAAA')",
        f"candidate(s={'A' * 100000!r})",
    }
    while len(cases) < 600:
        n = rng.randint(1, 1000)
        if rng.random() < 0.5 and n >= 20:
            unit = "".join(rng.choice("ACGT") for _ in range(10))
            s = unit + "".join(rng.choice("ACGT") for _ in range(n - 10)) + unit
        else:
            s = "".join(rng.choice("ACGT") for _ in range(n))
        assert 1 <= len(s) <= 100_000 and set(s) <= set("ACGT")
        cases.add(f"candidate(s={s!r})")
    return sorted(cases)
