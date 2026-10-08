def generate(seed: int = 0) -> list[str]:
    """Six hundred distinct n values in the stated range [0, 10^9]."""
    assert seed >= 0
    return [f"candidate(n={n})" for n in range(600)]
