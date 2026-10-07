from __future__ import annotations

DOMAIN_SIZE = 64


def generate(seed: int = 0) -> list[str]:
    return [
        f"candidate(coordinates={chr(97 + col) + str(row)!r})"
        for col in range(8)
        for row in range(1, 9)
    ]
