import random


MOVES = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))


def make_tour(size: int, rng: random.Random) -> list[list[int]] | None:
    path = [(0, 0)]
    visited = {(0, 0)}

    while len(path) < size * size:
        row, col = path[-1]
        candidates = [
            (row + dr, col + dc)
            for dr, dc in MOVES
            if 0 <= row + dr < size
            and 0 <= col + dc < size
            and (row + dr, col + dc) not in visited
        ]
        if not candidates:
            return None
        rng.shuffle(candidates)
        candidates.sort(
            key=lambda cell: sum(
                0 <= cell[0] + dr < size
                and 0 <= cell[1] + dc < size
                and (cell[0] + dr, cell[1] + dc) not in visited
                for dr, dc in MOVES
            )
        )
        path.append(candidates[0])
        visited.add(candidates[0])

    grid = [[0] * size for _ in range(size)]
    for move_number, (row, col) in enumerate(path):
        grid[row][col] = move_number
    return grid


def is_tour(grid: list[list[int]]) -> bool:
    size = len(grid)
    positions = [None] * (size * size)
    for row in range(size):
        for col in range(size):
            positions[grid[row][col]] = (row, col)
    if grid[0][0] != 0:
        return False
    for current, following in zip(positions, positions[1:]):
        if current is None or following is None:
            return False
        row_delta = abs(current[0] - following[0])
        col_delta = abs(current[1] - following[1])
        if sorted((row_delta, col_delta)) != [1, 2]:
            return False
    return True


def generate(seed: int = 0) -> list[str]:
    """Include real tours and distinct invalid permutations under the original constraints."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    index = 0

    while len(calls) < 300:
        size = 5 + index % 3
        grid = make_tour(size, rng)
        index += 1
        if grid is None:
            continue
        assert grid[0][0] == 0 and is_tour(grid)
        call = f"candidate(grid={grid!r})"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    while len(calls) < 600:
        size = 3 + index % 5
        # Shuffle after fixing the required start cell.
        remainder = list(range(1, size * size))
        rng.shuffle(remainder)
        values = [0, *remainder]
        grid = [values[row * size : (row + 1) * size] for row in range(size)]
        if is_tour(grid):
            continue
        assert grid[0][0] == 0
        assert sorted(value for row in grid for value in row) == list(
            range(size * size)
        )
        call = f"candidate(grid={grid!r})"
        index += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
