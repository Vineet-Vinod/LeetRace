"""All 512 possible boards are enumerated exactly once: each of the 9 cells has 2 choices, so the finite domain is 2^9."""

import itertools
import random


def generate(seed: int = 0) -> list[str]:
    random.Random(seed)
    calls = []
    for cells in itertools.product("BW", repeat=9):
        rows = [list(cells[index : index + 3]) for index in range(0, 9, 3)]
        calls.append(f"candidate(grid={rows!r})")
    assert len(calls) == 512
    assert len(set(calls)) == 512
    return calls
