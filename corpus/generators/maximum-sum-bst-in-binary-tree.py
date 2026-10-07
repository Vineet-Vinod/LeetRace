import random

EXAMPLES = [
    "candidate(root=tree_node([1, 4, 3, 2, 4, 2, 5, None, None, None, None, None, None, 4, 6]))",
    "candidate(root=tree_node([4, 3, None, 1, 2]))",
    "candidate(root=tree_node([-4, -2, -5]))",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = list(EXAMPLES)
    seen = set(calls)

    def emit(call: str) -> None:
        if call not in seen:
            calls.append(call)
            seen.add(call)

    def add(values):
        count = sum(v is not None for v in values)
        assert 1 <= count <= 40000 and all(
            v is None or -40000 <= v <= 40000 for v in values
        )
        # These complete level-order arrays or explicitly constructed chains are valid trees.
        pending = 1
        for v in values:
            assert pending > 0
            pending -= 1
            if v is not None:
                pending += 2
        emit(f"candidate(root=tree_node({values!r}))")

    add([-40000] * 40000)
    add([40000])
    add([-40000])
    add([0])
    add([i if i % 2 == 0 else None for i in range(1999)])
    while len(calls) < 600:
        n = rng.randint(1, 60)
        values = [rng.randint(-100, 100) for _ in range(n)]
        if rng.random() < 0.2:
            values = [-abs(v) - 1 for v in values]
        add(values)
    return calls
