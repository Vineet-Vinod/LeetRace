import random
from collections import deque


def make_tree(values: list[int], low: int, high: int):
    if low >= high:
        return None
    middle = (low + high - 1) // 2
    return (
        values[middle],
        make_tree(values, low, middle),
        make_tree(values, middle + 1, high),
    )


def level_order(values: list[int]) -> list[int | None]:
    root = make_tree(values, 0, len(values))
    result: list[int | None] = [root[0]]
    queue = deque([root])
    while queue:
        _, left, right = queue.popleft()
        for child in (left, right):
            if child is None:
                result.append(None)
            else:
                result.append(child[0])
                queue.append(child)
    while result[-1] is None:
        result.pop()
    return result


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], int]] = {
        ((2, 3, 4, 5, 6, 7), 9),
        ((2, 3, 4, 5, 6, 7), 28),
    }
    cases.add((tuple(range(-10_000, -1)) + (10_000,), 0))
    cases.add((tuple(range(-10_000, -1)) + (10_000,), 100_000))
    while len(cases) < 600:
        size = rng.randint(2, 100)
        values = tuple(sorted(rng.sample(range(-10_000, 10_001), size)))
        k = rng.randint(-100_000, 100_000)
        cases.add((values, k))
        cases.add((values, values[0] + values[-1]))
    calls = [
        f"candidate(root=tree_node({level_order(list(values))!r}), k={k})"
        for values, k in cases
    ]
    calls.extend(
        [
            "candidate(root=tree_node([5, 3, 6, 2, 4, None, 7]), k=9)",
            "candidate(root=tree_node([5, 3, 6, 2, 4, None, 7]), k=28)",
        ]
    )
    return list(dict.fromkeys(calls))
