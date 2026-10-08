import random


def generate(seed: int = 0) -> list[str]:
    """Use at least one guard and one wall at distinct valid grid positions."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    index = 0
    while len(calls) < 600:
        if index == 0:
            m, n = 1, 2
        else:
            m = 1 + index % 12
            n = 1 + (index * 7) % 12
            if m * n < 2:
                n = 2
        cells = [(row, col) for row in range(m) for col in range(n)]
        rng.shuffle(cells)
        guard_count = 1 + index % min(8, len(cells) - 1)
        wall_count = 1 + (index * 3) % (len(cells) - guard_count)
        guards = [list(cell) for cell in cells[:guard_count]]
        walls = [list(cell) for cell in cells[guard_count : guard_count + wall_count]]
        assert 2 <= m * n <= 100_000
        assert 1 <= len(guards) and 1 <= len(walls)
        assert len(guards) + len(walls) <= m * n
        assert not (set(map(tuple, guards)) & set(map(tuple, walls)))
        call = f"candidate(m={m}, n={n}, guards={guards!r}, walls={walls!r})"
        index += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
