def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(colors='AAABABB')",
        "candidate(colors='ABBBBBBBAAA')",
        f"candidate(colors={'A' * 100000!r})",
    }
    while len(cases) < 600:
        n = rng.randint(1, 1000)
        if rng.random() < 0.5:
            colors = "".join(rng.choice("AB") for _ in range(n))
        else:
            colors = "".join(
                char * rng.randint(1, 20)
                for char in rng.choices("AB", k=max(1, n // 10))
            )[:n]
        assert 1 <= len(colors) <= 100_000 and set(colors) <= set("AB")
        cases.add(f"candidate(colors={colors!r})")
    return sorted(cases)
