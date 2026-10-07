import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        length = rng.randint(1, 80)
        digits = "".join(str(rng.randint(1, 9)) for _ in range(length))
        n = ("-" if rng.random() < 0.3 else "") + digits
        x = rng.randint(1, 9)
        key = (n, x)
        if key not in seen:
            seen.add(key)
            assert (
                digits
                and digits[0] != "0"
                and all(c in "123456789" for c in digits)
                and 1 <= x <= 9
            )
            cases.append(f"candidate(n={n!r}, x={x})")
    return cases
