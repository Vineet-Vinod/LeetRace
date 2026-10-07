DOMAIN_SIZE = 510


def generate(seed: int = 0) -> list[str]:
    from itertools import product

    # The complete domain has sum(2**n, n=1..8) = 510 patterns.
    return [
        f"candidate(pattern={''.join(pattern)!r})"
        for length in range(1, 9)
        for pattern in product("ID", repeat=length)
    ]
