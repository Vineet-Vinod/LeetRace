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


def to_level_order(values: list[int]) -> list[int | None]:
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
    cases: set[tuple[int, ...]] = {(0, 1), (1, 2), (0, 1, 12, 48, 49)}
    cases.add(tuple(range(99)) + (100_000,))
    while len(cases) < 600:
        size = rng.randint(2, 100)
        values = tuple(sorted(rng.sample(range(0, 100_001), size)))
        cases.add(values)
    calls = [
        f"candidate(root=tree_node({to_level_order(list(values))!r}))"
        for values in cases
    ]
    calls.extend(
        [
            "candidate(root=tree_node([4, 2, 6, 1, 3]))",
            "candidate(root=tree_node([1, 0, 48, None, None, 12, 49]))",
        ]
    )
    return list(dict.fromkeys(calls))
