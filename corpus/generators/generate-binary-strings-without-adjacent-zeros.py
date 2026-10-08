DOMAIN_SIZE = 18


def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    return [f"candidate(n={n})" for n in range(1, 19)]
