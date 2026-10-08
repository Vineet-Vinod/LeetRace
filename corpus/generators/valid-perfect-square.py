from __future__ import annotations
import math
import random

EXAMPLE_CALLS = [
    "candidate(num=16)",
    "candidate(num=14)",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    squares = {
        EXAMPLE_CALLS[0],
        "candidate(num=1)",
        "candidate(num=2147395600)",
    }
    nonsquares = {
        EXAMPLE_CALLS[1],
        "candidate(num=2)",
        "candidate(num=2147483647)",
    }
    while len(squares) < 300:
        root = rng.randint(1, 46340)
        squares.add(f"candidate(num={root * root})")
    while len(nonsquares) < 300:
        number = rng.randint(1, 2_147_483_647)
        root = math.isqrt(number)
        if root * root == number:
            continue
        nonsquares.add(f"candidate(num={number})")
    assert len(squares) == 300 and len(nonsquares) == 300
    return sorted(squares | nonsquares)
