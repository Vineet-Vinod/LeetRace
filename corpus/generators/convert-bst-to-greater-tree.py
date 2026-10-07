import random
from collections import deque


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {
        (),
        (0,),
        (0, 1),
        (0, 1, 2, 3, 4, 5, 6, 7, 8),
        tuple(range(-5000, 5000)),
    }
    while len(cases) < 600:
        size = rng.randint(1, 60)
        cases.add(tuple(sorted(rng.sample(range(-10000, 10001), size))))

    def level_order(values: tuple[int, ...]) -> list[int | None]:
        if not values:
            return []
        result: list[int | None] = []
        queue = deque([(0, len(values))])
        while queue:
            interval = queue.popleft()
            if interval is None:
                result.append(None)
                continue
            lo, hi = interval
            if lo >= hi:
                result.append(None)
                continue
            mid = (lo + hi) // 2
            result.append(values[mid])
            queue.append((lo, mid))
            queue.append((mid + 1, hi))
        while result and result[-1] is None:
            result.pop()
        return result

    calls = [
        f"(lambda root: (repr(candidate(root)), repr(root)))(tree_node({level_order(values)!r}))"
        for values in cases
    ]
    right_chain = [
        value for pair in zip(range(1, 10_001), [None] * 10_000) for value in pair
    ]
    right_chain.pop()
    left_chain = [10_000]
    for value in range(9_999, 0, -1):
        left_chain.extend((value, None))
    calls.extend(
        f"(lambda root: (repr(candidate(root)), repr(root)))(tree_node({tree!r}))"
        for tree in (right_chain, left_chain)
    )
    assert all(
        0 <= len(values) <= 10_000
        and len(set(values)) == len(values)
        and all(-10_000 <= value <= 10_000 for value in values)
        for values in cases
    )
    return calls
