def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = {"candidate(s='011010', minJump=2, maxJump=3)"}
    while len(cases) < 600:
        n = rng.randint(2, 200)
        bits = ["0"] + ["".join(rng.choice("01") for _ in range(n - 2))] + ["0"]
        lo = rng.randint(1, n - 1)
        hi = rng.randint(lo, n - 1)
        cases.add(f"candidate(s={''.join(bits)!r}, minJump={lo}, maxJump={hi})")
    return sorted(cases)
