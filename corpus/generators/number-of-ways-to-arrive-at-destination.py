def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(n=1, roads=[])",
        "candidate(n=4, roads=[[0, 1, 1], [1, 3, 1], [0, 2, 1], [2, 3, 1]])",
        "candidate(n=4, roads=[[0, 1, 1], [1, 3, 1], [0, 2, 1], [2, 3, 2], [0, 3, 9]])",
        f"candidate(n=200, roads={[[node, node + 1, 1] for node in range(199)]!r})",
    }

    while len(cases) < 250:
        layers = rng.randint(1, 99)
        node_count = 2 * layers + 2
        roads = []
        first_layer = [1, 2]
        first_cost = rng.randint(1, 10**9)
        roads.extend([[0, node, first_cost] for node in first_layer])
        for layer in range(1, layers):
            previous = [2 * layer - 1, 2 * layer]
            current = [2 * layer + 1, 2 * layer + 2]
            cost = rng.randint(1, 10**9)
            roads.extend(
                [[left, right, cost] for left in previous for right in current]
            )
        last = node_count - 1
        roads.extend([[node_count - 2, last, 1], [node_count - 3, last, 1]])
        assert 1 <= node_count <= 200
        assert len({tuple(sorted(road[:2])) for road in roads}) == len(roads)
        assert all(1 <= cost <= 10**9 for _, _, cost in roads)
        cases.add(f"candidate(n={node_count}, roads={roads!r})")

    while len(cases) < 600:
        n = rng.randint(1, 30)
        edge_set = set()
        for node in range(1, n):
            parent = rng.randrange(node)
            edge_set.add((parent, node))
        for first in range(n):
            for second in range(first + 1, n):
                if rng.random() < 0.08:
                    edge_set.add((first, second))
        roads = [
            [first, second, rng.randint(1, 10**9)] for first, second in sorted(edge_set)
        ]
        assert len(roads) >= n - 1
        assert len({tuple(sorted(road[:2])) for road in roads}) == len(roads)
        assert all(1 <= time <= 10**9 for _, _, time in roads)
        cases.add(f"candidate(n={n}, roads={roads!r})")
    assert len(cases) == 600
    return sorted(cases)
