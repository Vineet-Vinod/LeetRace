def generate(seed: int = 0) -> list[str]:
    """Generate 600 distinct pairs in the stated 1..100 ranges."""
    assert seed >= 0
    return [
        f"candidate(numBottles={1 + i // 100}, numExchange={1 + i % 100})"
        for i in range(600)
    ]
