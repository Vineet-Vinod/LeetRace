import random


def generate(seed: int = 0) -> list[str]:
    """Use nearby targets to keep each BFS modest; deadends are unique and exclude target."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    pool = [f"{value:04d}" for value in range(30)]
    while len(calls) < 600:
        target = f"000{rng.randrange(10)}"
        candidates = [state for state in pool if state not in (target, "0000")]
        deadends = sorted(rng.sample(candidates, 1 + i % min(7, len(candidates))))
        call = f"candidate(deadends={deadends!r}, target={target!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
