import random


def generate(seed: int = 0) -> list[str]:
    """Generate unique dislike edges with 1-based endpoints and no self-loops."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        n = 1 + i % 30
        candidates = [(a, b) for a in range(1, n + 1) for b in range(a + 1, n + 1)]
        rng.shuffle(candidates)
        edges = (
            [list(edge) for edge in candidates[: i % min(40, len(candidates) + 1)]]
            if candidates
            else []
        )
        call = f"candidate(n={n}, dislikes={edges!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
