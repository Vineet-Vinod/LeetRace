import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        num = "".join(str(rng.randrange(10)) for _ in range(rng.randint(1, 100)))
        if num not in seen:
            seen.add(num)
            assert num.isdigit() and 1 <= len(num) <= 100000
            cases.append(f"candidate(num={num!r})")
    return cases
