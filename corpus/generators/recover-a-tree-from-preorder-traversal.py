import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        calls[
            "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        ] = None

    # Build a binary tree with the one-child-is-left promise before serialization.
    def traversal(size: int, chain: bool = False) -> str:
        values = [rng.randint(1, 10**9) for _ in range(size)]
        children = [[] for _ in range(size)]
        available = [0]
        for i in range(1, size):
            parent = i - 1 if chain else rng.choice(available)
            children[parent].append(i)
            if len(children[parent]) == 2:
                available.remove(parent)
            available.append(i)
        parts = []
        stack = [(0, 0)]
        while stack:
            v, depth = stack.pop()
            parts.append("-" * depth + str(values[v]))
            for child in reversed(children[v]):
                stack.append((child, depth + 1))
        assert (
            len(values) == size
            and all(1 <= v <= 10**9 for v in values)
            and all(len(c) <= 2 for c in children)
        )
        return "".join(parts)

    add(traversal="1")
    add(traversal="1000000000")
    add(traversal=traversal(1000, True))
    add(traversal=traversal(1000))
    while len(calls) < 600:
        size = rng.randint(1, 45)
        add(traversal=traversal(size, len(calls) % 5 == 0))
    assert len(calls) == 600
    return list(calls)
