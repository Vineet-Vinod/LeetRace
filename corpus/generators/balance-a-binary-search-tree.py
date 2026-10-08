import random
from collections import deque


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases, seen = [], set()
    for level in ([1, None, 2, None, 3, None, 4], [2, 1, 3]):
        key = tuple(level)
        seen.add(key)
        cases.append(f"candidate(root=tree_node({level!r}))")
    cases.append(
        "candidate(root=tree_node([value if value % 2 else None for value in range(1, 20000)]))"
    )
    while len(cases) < 600:
        n = rng.randint(1, 45)
        values = sorted(rng.sample(range(1, 100000), n))
        root = None
        for value in values:
            if root is None:
                root = [value, None, None]
                continue
            node = root
            while True:
                side = 1 if value < node[0] else 2
                if node[side] is None:
                    node[side] = [value, None, None]
                    break
                node = node[side]
        queue = deque([root])
        level = []
        while queue:
            node = queue.popleft()
            if node is None:
                level.append(None)
            else:
                level.append(node[0])
                queue.extend((node[1], node[2]))
        while level and level[-1] is None:
            level.pop()
        key = tuple(level)
        if key not in seen:
            seen.add(key)
            assert len(values) == n and values == sorted(set(values))
            cases.append(f"candidate(root=tree_node({level!r}))")
    return cases
