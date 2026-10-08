import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(edges: list[list[int]]) -> None:
        n = len(edges)
        assert 3 <= n <= 1000 and len({tuple(e) for e in edges}) == n
        assert all(
            len(e) == 2 and 1 <= e[0] <= n and 1 <= e[1] <= n and e[0] != e[1]
            for e in edges
        )

        def is_tree(removed: int) -> bool:
            degree = [0] * (n + 1)
            adj: list[list[int]] = [[] for _ in range(n + 1)]
            for i, (a, b) in enumerate(edges):
                if i != removed:
                    degree[b] += 1
                    adj[a].append(b)
            roots = [i for i in range(1, n + 1) if degree[i] == 0]
            if len(roots) != 1 or any(
                degree[i] != 1 for i in range(1, n + 1) if i != roots[0]
            ):
                return False
            visited = {roots[0]}
            order = [roots[0]]
            for a in order:
                for b in adj[a]:
                    if b in visited:
                        return False
                    visited.add(b)
                    order.append(b)
            return len(visited) == n

        assert any(is_tree(i) for i in range(n - 1, -1, -1))
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in [("edges", edges)])
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(edges=[[1, 2], [1, 3], [2, 3]])
    add(edges=[[i, i + 1] for i in range(1, 1000)] + [[1000, 1]])
    add(edges=[[1, i] for i in range(2, 1001)] + [[999, 1000]])
    add(edges=[[1, 2], [1, 3], [2, 3]])
    add(edges=[[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]])
    while len(calls) < 600:
        n = rng.randint(3, 35)
        labels = rng.sample(range(1, n + 1), n)
        edges = [[labels[rng.randrange(i)], labels[i]] for i in range(1, n)]
        existing = {tuple(e) for e in edges}
        extra = rng.choice(
            [
                (u, v)
                for u in labels
                for v in labels
                if u != v and (u, v) not in existing
            ]
        )
        # The first n-1 edges connect each new node to one earlier parent.
        edges.append(list(extra))
        rng.shuffle(edges)
        add(edges=edges)
    return calls
