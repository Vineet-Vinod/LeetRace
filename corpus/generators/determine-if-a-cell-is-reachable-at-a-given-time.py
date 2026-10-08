import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: coordinates 1..10^9; t 0..10^9."""
    rng = random.Random(seed)
    calls = {
        "candidate(sx=2, sy=4, fx=7, fy=7, t=6)",
        "candidate(sx=3, sy=1, fx=7, fy=3, t=3)",
        "candidate(sx=1, sy=1, fx=1, fy=1, t=1)",
    }
    while len(calls) < 600:
        sx, sy = rng.randint(1, 10**9), rng.randint(1, 10**9)
        fx, fy = rng.randint(1, 10**9), rng.randint(1, 10**9)
        t = rng.randint(0, 10**9)
        calls.add(f"candidate(sx={sx}, sy={sy}, fx={fx}, fy={fy}, t={t})")
    return sorted(calls)
