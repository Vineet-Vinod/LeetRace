def generate(seed: int = 0) -> list[str]:
    """All 600 inputs are distinct legal values of n; this task's output depends only on n."""
    assert seed >= 0
    return [f"candidate(n={n})" for n in range(1, 601)]
