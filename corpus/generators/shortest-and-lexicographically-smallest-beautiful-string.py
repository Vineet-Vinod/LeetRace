def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(s='100011001', k=3)",
        "candidate(s='1011', k=2)",
        "candidate(s='000', k=1)",
        "candidate(s='1' * 100, k=100)",
    }
    while len(cases) < 600:
        n = rng.randint(1, 100)
        s = "".join(rng.choice("01") for _ in range(n))
        k = rng.randint(1, n)
        assert len(s) == n and set(s) <= {"0", "1"} and 1 <= k <= len(s)
        cases.add(f"candidate(s={s!r}, k={k})")
    return sorted(cases)
