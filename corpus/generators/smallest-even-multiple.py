from __future__ import annotations

DOMAIN_SIZE = 150


def generate(seed: int = 0) -> list[str]:
    return [f"candidate(n={value})" for value in range(1, 151)]
