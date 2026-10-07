def generate(seed: int = 0) -> list[str]:
    """Generate 599 small n values plus the maximum n=10^6 boundary."""
    assert seed >= 0
    return [f"candidate(n={n})" for n in range(1, 600)] + ["candidate(n=1000000)"]
