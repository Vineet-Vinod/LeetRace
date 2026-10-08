import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        ((0, -1), (1, 0), (2, 0), (3, 2), (4, 2)),
        ((0, -1), (1, 0), (2, 0), (3, 1), (4, 1)),
    }
    while len(cases) < 600:
        n = rng.randint(1, 30)
        children = [[] for _ in range(n)]
        parents = [-1]
        for node in range(1, n):
            eligible = [parent for parent in range(node) if len(children[parent]) < 2]
            parent = rng.choice(eligible)
            parents.append(parent)
            children[parent].append(node)
        order: list[int] = []
        stack = [0]
        while stack:
            node = stack.pop()
            order.append(node)
            stack.extend(reversed(children[node]))
        records = [(node, parents[node]) for node in order]
        if rng.random() < 0.5 and n > 2:
            rng.shuffle(records[1:])
            tail = records[1:]
            rng.shuffle(tail)
            records = records[:1] + tail
        cases.add(tuple(records))
    return [
        f"candidate(nodes={[list(record) for record in records]!r})"
        for records in cases
    ]
