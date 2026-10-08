import random


def generate(seed: int = 0) -> list[str]:
    """Generate an even number of positive piles whose total is odd."""
    rng = random.Random(seed)
    boundary = [1] * 499 + [2]
    calls = [
        f"candidate(piles={boundary!r})",
        f"candidate(piles={[500] + [1] * 499!r})",
    ]
    seen = set(calls)
    i = 0
    while len(calls) < 600:
        n = 2 + 2 * (i % 25)
        piles = [rng.randrange(1, 501) for _ in range(n)]
        if sum(piles) % 2 == 0:
            piles[0] = piles[0] % 500 + 1
        call = f"candidate(piles={piles!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
