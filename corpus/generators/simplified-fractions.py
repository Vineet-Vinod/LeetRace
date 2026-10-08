def generate(seed: int = 0) -> list[str]:
    # The full legal scalar domain n=1..100 is finite and enumerated.
    return [f"candidate(n={n})" for n in range(1, 101)]


DOMAIN_SIZE = 100
