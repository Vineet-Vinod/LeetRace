def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(binary='0')",
        "candidate(binary='1')",
        "candidate(binary='00')",
        "candidate(binary='01')",
        "candidate(binary='000110')",
        f"candidate(binary={'0' * 100000!r})",
        f"candidate(binary={'1' * 100000!r})",
        f"candidate(binary={('01' * 50000)!r})",
        f"candidate(binary={('1' * 50000 + '0' + '1' * 49999)!r})",
    }
    while len(cases) < 600:
        binary = "".join(rng.choice("01") for _ in range(rng.randint(1, 100)))
        assert 1 <= len(binary) <= 100000 and set(binary) <= {"0", "1"}
        cases.add(f"candidate(binary={binary!r})")
    assert len(cases) == 600
    return sorted(cases)
