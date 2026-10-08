import random
from collections import deque


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], int]] = {
        ((1, 4, 2, 3), 5),
        ((2, 1, 5, 4), 3),
        ((2, 1, 5, 3), 4),
    }
    while len(cases) < 600:
        size = rng.randint(1, 15)
        values = tuple(rng.sample(range(1, 101), size))
        available = [value for value in range(1, 101) if value not in values]
        cases.add((values, rng.choice(available)))

    def encode(values: tuple[int, ...]) -> list[int | None]:
        stack: list[dict[str, object]] = []
        root: dict[str, object] | None = None
        for value in values:
            node: dict[str, object] = {"val": value, "left": None, "right": None}
            last: dict[str, object] | None = None
            while stack and int(stack[-1]["val"]) < value:
                last = stack.pop()
            node["left"] = last
            if stack:
                stack[-1]["right"] = node
            else:
                root = node
            stack.append(node)
        result: list[int | None] = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node is None:
                result.append(None)
                continue
            result.append(int(node["val"]))
            queue.append(node["left"])
            queue.append(node["right"])
        while result and result[-1] is None:
            result.pop()
        return result

    return [
        f"candidate(root=tree_node({encode(values)!r}), val={value})"
        for values, value in cases
    ]
