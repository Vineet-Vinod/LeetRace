def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases: set[str] = set()

    def add(n: int, shape: str) -> None:
        assert 1 <= n <= 3000
        left = [-1] * n
        right = [-1] * n
        if shape == "left":
            for node in range(n - 1):
                left[node] = node + 1
        elif shape == "right":
            for node in range(n - 1):
                right[node] = node + 1
        elif shape == "balanced":
            slots = [(0, 0)]
            next_node = 1
            while next_node < n:
                parent, side = slots.pop(0)
                if side == 0:
                    left[parent] = next_node
                else:
                    right[parent] = next_node
                slots.extend(((next_node, 0), (next_node, 1)))
                next_node += 1
        else:
            slots = [(0, 0), (0, 1)]
            for node in range(1, n):
                slot_index = rng.randrange(len(slots))
                parent, side = slots.pop(slot_index)
                if side == 0:
                    left[parent] = node
                else:
                    right[parent] = node
                slots.extend(((node, 0), (node, 1)))

        inorder_nodes: list[int] = []
        stack: list[int] = []
        current = 0
        while current != -1 or stack:
            while current != -1:
                stack.append(current)
                current = left[current]
            current = stack.pop()
            inorder_nodes.append(current)
            current = right[current]
        values = [value - n // 2 for value in range(n)]
        node_value = {node: values[index] for index, node in enumerate(inorder_nodes)}

        postorder: list[int] = []
        pending = [(0, False)]
        while pending:
            node, visited = pending.pop()
            if visited:
                postorder.append(node_value[node])
                continue
            pending.append((node, True))
            if right[node] != -1:
                pending.append((right[node], False))
            if left[node] != -1:
                pending.append((left[node], False))
        inorder = [node_value[node] for node in inorder_nodes]
        assert len(set(inorder)) == n and len(postorder) == n
        assert all(-3000 <= value <= 3000 for value in inorder)
        cases.add(f"candidate(inorder={inorder!r}, postorder={postorder!r})")

    add(5, "random")
    add(1, "left")
    add(3000, "left")
    add(3000, "right")
    add(3000, "balanced")
    add(3000, "random")
    while len(cases) < 600:
        n = rng.randint(1, 250)
        add(n, rng.choice(("random", "balanced", "left", "right")))
    result = list(cases)
    rng.shuffle(result)
    return result
