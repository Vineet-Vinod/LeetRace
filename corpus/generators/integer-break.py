def generate(seed: int = 0) -> list[str]:
    """Enumerate the complete legal input domain n=2..58 (57 distinct inputs)."""
    assert seed >= 0
    return [f"candidate(n={n})" for n in range(2, 59)]


DOMAIN_SIZE = 57
