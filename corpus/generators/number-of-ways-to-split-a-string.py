import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {"10101", "1001", "0000", "111", "010", "0" * 100_000}
    while len(cases) < 600:
        cases.add("".join(rng.choice("01") for _ in range(rng.randint(3, 100))))
    assert all(3 <= len(s) <= 100_000 and set(s) <= {"0", "1"} for s in cases)
    return [f"candidate(s={s!r})" for s in sorted(cases)]
