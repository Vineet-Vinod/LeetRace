def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    alphabet = "abCD,.Z"
    cases = {
        "candidate(s='PAYPALISHIRING', numRows=3)",
        "candidate(s='PAYPALISHIRING', numRows=4)",
        "candidate(s='A', numRows=1)",
        "candidate(s='z'*1000, numRows=1000)",
    }
    while len(cases) < 600:
        n = rng.randint(1, 1000)
        s = "".join(rng.choice(alphabet) for _ in range(n))
        rows = rng.randint(1, 1000)
        assert 1 <= len(s) <= 1000 and 1 <= rows <= 1000 and set(s) <= set(alphabet)
        cases.add(f"candidate(s={s!r}, numRows={rows})")
    return sorted(cases)
