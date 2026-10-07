from __future__ import annotations
import random

EXAMPLE_CALLS = [
    "candidate(rec1=[0, 0, 2, 2], rec2=[1, 1, 3, 3])",
    "candidate(rec1=[0, 0, 1, 1], rec2=[1, 0, 2, 1])",
    "candidate(rec1=[0, 0, 1, 1], rec2=[2, 2, 3, 3])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    overlapping = {
        EXAMPLE_CALLS[0],
        "candidate(rec1=[-1000000000, -1000000000, -999999999, -999999999], rec2=[-1000000000, -1000000000, -999999999, -999999999])",
    }
    separate = {
        EXAMPLE_CALLS[1],
        EXAMPLE_CALLS[2],
        "candidate(rec1=[-1000000000, 0, -999999999, 1], rec2=[999999999, 0, 1000000000, 1])",
    }
    while len(overlapping) < 300:
        x, y = rng.randint(-1000, 1000), rng.randint(-1000, 1000)
        width, height = rng.randint(1, 100), rng.randint(1, 100)
        dx, dy = rng.randint(1 - width, width - 1), rng.randint(1 - height, height - 1)
        first = [x, y, x + width, y + height]
        second = [x + dx, y + dy, x + dx + width, y + dy + height]
        overlapping.add(f"candidate(rec1={first!r}, rec2={second!r})")
    while len(separate) < 300:
        x, y = rng.randint(-1000, 1000), rng.randint(-1000, 1000)
        width, height = rng.randint(1, 100), rng.randint(1, 100)
        other_width, other_height = rng.randint(1, 100), rng.randint(1, 100)
        first = [x, y, x + width, y + height]
        second = [x + width + 1, y, x + width + 1 + other_width, y + other_height]
        separate.add(f"candidate(rec1={first!r}, rec2={second!r})")
    assert len(overlapping) == 300 and len(separate) == 300
    return sorted(overlapping | separate)
