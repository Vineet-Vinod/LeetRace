import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        n = rng.randint(1, 6)
        price = [rng.randint(0, 10) for _ in range(n)]
        needs = [rng.randint(0, 10) for _ in range(n)]
        special = []
        for _ in range(rng.randint(1, 12)):
            quantities = [rng.randint(0, 5) for _ in range(n)]
            if not any(quantities):
                quantities[rng.randrange(n)] = 1
            special.append(quantities + [rng.randint(0, 50)])
        key = (tuple(price), tuple(map(tuple, special)), tuple(needs))
        if key not in seen:
            seen.add(key)
            assert all(0 <= v <= 10 for v in price + needs) and all(
                len(o) == n + 1 and any(o[:n]) and 0 <= o[-1] <= 50 for o in special
            )
            cases.append(
                f"candidate(price={price!r}, special={special!r}, needs={needs!r})"
            )
    return cases
