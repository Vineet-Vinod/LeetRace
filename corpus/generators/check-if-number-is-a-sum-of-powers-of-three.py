import random


def generate(seed: int = 0) -> list[str]:
    r = random.Random(seed)
    vals = {1, 2, 3, 4, 5, 10**7}
    # Every base-three expansion using only digits 0 and 1 is representable.
    for _ in range(300):
        digits = [r.randrange(2) for _ in range(r.randint(1, 15))]
        vals.add(sum(d * 3**i for i, d in enumerate(digits)) or 1)
    while len(vals) < 600:
        digits = [r.randrange(3) for _ in range(r.randint(1, 15))]
        n = sum(d * 3**i for i, d in enumerate(digits))
        if n <= 10**7:
            vals.add(n or 1)
    vals.add(10**7)
    selected = []
    for n in sorted(vals):
        if n not in selected:
            selected.append(n)
        if len(selected) == 600:
            break
    if 10**7 not in selected:
        selected[-1] = 10**7
    return [f"candidate(n={n})" for n in selected]
