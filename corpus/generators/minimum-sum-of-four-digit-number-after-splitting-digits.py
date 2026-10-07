import random


def generate(seed: int = 0) -> list[str]:
    """All generated arguments stay within the statement bounds and follow the problem guarantees."""
    r = random.Random(seed)
    vals = [2932, 4009, 1000, 9999]
    seen = set(vals)
    while len(vals) < 600:
        n = r.randint(1000, 9999)
        if n not in seen:
            seen.add(n)
            vals.append(n)
    return [f"candidate(num={n})" for n in vals]
