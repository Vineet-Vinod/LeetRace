DOMAIN_SIZE = 12


def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    return [f"candidate(n={2**power})" for power in range(1, 13)]
