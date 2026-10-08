def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        size = rng.randint(1, 60)
        order = list(range(size))
        rng.shuffle(order)
        left = [-1] * size
        right = [-1] * size
        available = [0]
        for node in range(1, size):
            parent = rng.choice(available)
            side = rng.choice([0, 1])
            while (left[parent] if side == 0 else right[parent]) != -1:
                side = 1 - side
            if side == 0:
                left[parent] = node
            else:
                right[parent] = node
            if left[parent] != -1 and right[parent] != -1:
                available.remove(parent)
            available.append(node)
        preorder = []
        inorder = []

        def visit(node: int) -> None:
            if node < 0:
                return
            preorder.append(order[node])
            visit(left[node])
            inorder.append(order[node])
            visit(right[node])

        visit(0)
        cases.add(f"candidate(preorder={preorder!r}, inorder={inorder!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    inorder = list(range(3000))
    preorder = []

    def visit(left: int, right: int) -> None:
        if left >= right:
            return
        middle = (left + right) // 2
        preorder.append(middle)
        visit(left, middle)
        visit(middle + 1, right)

    visit(0, 3000)
    assert len(preorder) == len(inorder) == 3000
    boundary = f"candidate(preorder={preorder!r}, inorder={inorder!r})"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
