def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    wins = set()
    losses = set()
    while len(wins) < 300 or len(losses) < 300:
        n = rng.choice(range(1, 100, 2))
        values = list(range(1, n + 1))
        rng.shuffle(values)
        if len(wins) < 300 and n >= 5:
            x = values[2]
            wins.add(f"candidate(root=tree_node({values!r}),n={n},x={x})")
        if len(losses) < 300:
            if n == 1:
                index = 0
            else:
                subtree = [1] * n
                for node in range(n - 1, -1, -1):
                    left, right = 2 * node + 1, 2 * node + 2
                    if left < n:
                        subtree[node] += subtree[left]
                    if right < n:
                        subtree[node] += subtree[right]
                index = next(
                    node
                    for node in range(n)
                    if max(
                        n - subtree[node],
                        subtree[2 * node + 1] if 2 * node + 1 < n else 0,
                        subtree[2 * node + 2] if 2 * node + 2 < n else 0,
                    )
                    <= n // 2
                )
            x = values[index]
            losses.add(f"candidate(root=tree_node({values!r}),n={n},x={x})")
    return sorted(wins | losses)
