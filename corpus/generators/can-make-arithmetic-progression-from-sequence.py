from __future__ import annotations
import random

EXAMPLE_CALLS = [
    "candidate(arr=[3, 5, 1])",
    "candidate(arr=[1, 2, 4])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    possible = {
        EXAMPLE_CALLS[0],
        "candidate(arr=[-1000000, 0, 1000000])",
        f"candidate(arr={list(range(1000))!r})",
    }
    impossible = {
        EXAMPLE_CALLS[1],
        "candidate(arr=[0, 0, 1])",
        "candidate(arr=[-1000000, 999999, 1000000])",
    }

    def is_progression(values: list[int]) -> bool:
        ordered = sorted(values)
        difference = ordered[1] - ordered[0]
        return all(
            ordered[i] - ordered[i - 1] == difference for i in range(2, len(ordered))
        )

    while len(possible) < 300:
        length = 1000 if rng.random() < 0.02 else rng.randint(2, 1000)
        difference = rng.randint(-1000, 1000)
        start = rng.randint(-1_000_000, 1_000_000)
        values = [start + i * difference for i in range(length)]
        if min(values) < -1_000_000 or max(values) > 1_000_000:
            continue
        rng.shuffle(values)
        possible.add(f"candidate(arr={values!r})")

    while len(impossible) < 300:
        length = 1000 if rng.random() < 0.02 else rng.randint(3, 1000)
        values = [rng.randint(-1_000_000, 1_000_000) for _ in range(length)]
        if is_progression(values):
            values[-1] = values[-1] + 1 if values[-1] < 1_000_000 else values[-1] - 1
        rng.shuffle(values)
        impossible.add(f"candidate(arr={values!r})")

    assert len(possible) == 300 and len(impossible) == 300
    return sorted(possible | impossible)
