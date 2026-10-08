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
    assert values
    assert values == sorted(values)
    assert len(values) == len(set(values))
    root = make_tree(values, 0, len(values))
    assert root is not None
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
    calls = {
        "candidate(root=tree_node([4, 2, 5, 1, 3]), target=3.714286)",
        "candidate(root=tree_node([1]), target=4.428571)",
        "candidate(root=tree_node([4, 2, 5, 1, 3]), target=3.5)",
        "candidate(root=tree_node([0]), target=-1000000000.0)",
        "candidate(root=tree_node([1000000000]), target=1000000000.0)",
    }

    maximum_tree = list(range(10_000))
    calls.add(f"candidate(root=tree_node({level_order(maximum_tree)!r}), target=0.0)")
    calls.add(
        f"candidate(root=tree_node({level_order(maximum_tree)!r}), target=1000000000.0)"
    )

    while len(calls) < 600:
        size = rng.randint(1, 100)
        values = sorted(rng.sample(range(0, 1_000_000_001), size))
        target = round(rng.uniform(-1_000_000_000, 1_000_000_000), 6)
        assert 1 <= len(values) <= 10_000
        assert len(values) == len(set(values))
        assert all(0 <= value <= 1_000_000_000 for value in values)
        assert -1_000_000_000 <= target <= 1_000_000_000
        calls.add(
            f"candidate(root=tree_node({level_order(values)!r}), target={target!r})"
        )

    result = sorted(calls)
    assert 500 <= len(result) <= 999
    assert len(result) == len(set(result))
    return result
