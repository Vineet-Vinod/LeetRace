import random


def generate(seed: int = 0) -> list[str]:
    """Use sorted unique arrays with values in the original range [2, 10^9]."""
    rng = random.Random(seed)
    cases = {
        "candidate(arr=[2])",
        "candidate(arr=[2, 4])",
        "candidate(arr=[2, 4, 5, 10])",
    }
    cases.add(f"candidate(arr={[2, 4, 100_000, 10**9]!r})")
    while len(cases) < 600:
        size = rng.randint(1, 30)
        values = sorted(rng.sample(range(2, 1_000_000_001), size))
        cases.add(f"candidate(arr={values!r})")
    assert len(cases) == 600
    return sorted(cases)
