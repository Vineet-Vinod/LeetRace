def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: full finite domain is k=2..9 and n=1..60, hence 8*60=480 input pairs, enumerated completely."""
    # The full legal domain has 8 * 60 = 480 input pairs.
    return [f"candidate(k={k}, n={n})" for k in range(2, 10) for n in range(1, 61)]


DOMAIN_SIZE = 480
