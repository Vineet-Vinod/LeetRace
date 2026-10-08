def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)

    def encode(root):
        if root is None:
            return []
        out = []
        q = [root]
        while q:
            node = q.pop(0)
            out.append(node[0] if node else None)
            if node:
                q.extend([node[1], node[2]])
        while out and out[-1] is None:
            out.pop()
        return out

    def balanced(vals):
        if not vals:
            return None
        mid = len(vals) // 2
        return [vals[mid], balanced(vals[:mid]), balanced(vals[mid + 1 :])]

    cases = {
        f"candidate(root=tree_node({encode(balanced(list(range(10000))))!r}), low=0, high=9999)",
        "candidate(root=tree_node([10000]), low=10000, high=10000)",
        "candidate(root=tree_node([1, 0, 2]), low=1, high=2)",
        "candidate(root=tree_node([3, 0, 4, None, 2, None, None, 1]), low=1, high=3)",
    }
    while len(cases) < 600:
        n = rng.randint(1, 100)
        vals = sorted(rng.sample(range(0, 10001), n))
        root = balanced(vals)
        low = rng.randint(0, 10000)
        high = rng.randint(low, 10000)
        tree = encode(root)
        assert (
            1 <= len(vals) <= 10000
            and len(set(vals)) == len(vals)
            and all(0 <= value <= 10000 for value in vals)
            and 0 <= low <= high <= 10000
        )
        cases.add(f"candidate(root=tree_node({tree!r}), low={low}, high={high})")
    return sorted(cases)
