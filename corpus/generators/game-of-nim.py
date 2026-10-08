def generate(seed: int = 0) -> list[str]:
    import random
    from functools import reduce
    from operator import xor

    rng = random.Random(seed)
    wins = {"candidate(piles=[1])", "candidate(piles=[7, 7, 7, 7, 7, 7, 7])"}
    losses = {"candidate(piles=[1, 1])", "candidate(piles=[1, 2, 3])"}
    while len(wins) < 300:
        piles = [rng.randint(1, 7) for _ in range(rng.randint(1, 7))]
        if reduce(xor, piles, 0) == 0:
            piles[-1] = piles[-1] % 7 + 1
        assert 1 <= len(piles) <= 7 and all(1 <= pile <= 7 for pile in piles)
        wins.add(f"candidate(piles={piles!r})")
    while len(losses) < 300:
        piles = [rng.randint(1, 7) for _ in range(rng.randint(1, 6))]
        last = reduce(xor, piles, 0)
        if not 1 <= last <= 7:
            continue
        piles.append(last)
        assert 2 <= len(piles) <= 7 and reduce(xor, piles, 0) == 0
        losses.add(f"candidate(piles={piles!r})")
    return sorted(wins | losses)
