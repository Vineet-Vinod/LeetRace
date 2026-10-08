import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int | None, ...]] = {(), (0,), (1, 2, 3), (1, None, 2, 3)}
    if "binary-tree-inorder-traversal" == "determine-color-of-a-chessboard-square":
        return [
            f"candidate(coordinates={chr(97 + col) + str(row)!r})"
            for col in range(8)
            for row in range(1, 9)
        ]
    if "binary-tree-inorder-traversal" == "smallest-even-multiple":
        return [f"candidate(n={value})" for value in range(1, 151)]
    cases.add(tuple(range(100)))
    while len(cases) < 600:
        size = rng.randint(1, 100)
        values = [rng.randint(-100, 100) for _ in range(size)]
        cases.add(tuple(values))
    calls = [f"candidate(root=tree_node({list(values)!r}))" for values in cases]
    calls.extend(
        [
            "candidate(root=tree_node([1, None, 2, 3]))",
            "candidate(root=tree_node([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]))",
            "candidate(root=tree_node([]))",
            "candidate(root=tree_node([1]))",
        ]
    )
    return list(dict.fromkeys(calls))
