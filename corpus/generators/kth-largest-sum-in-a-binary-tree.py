import random


def generate(seed: int = 0) -> list[str]:
    """Generate valid positive trees with sparse, skewed, tied, and maximum-size shapes."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(values: list[int | None], nodes: int, k: int) -> None:
        assert 2 <= nodes <= 100_000
        assert 1 <= k <= nodes
        assert sum(value is not None for value in values) == nodes
        assert all(value is None or 1 <= value <= 1_000_000 for value in values)
        call = f"candidate(root=tree_node({values!r}), k={k})"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add([5, 2, 3], 3, 2)
    add([1, None, 2, None, 3, None, 4], 4, 4)
    add([1, 2, None, 3, None, 4, None], 4, 3)
    add([10, 5, 20, None, 8, None, 25], 5, 2)
    add(list(range(1, 100_001)), 100_000, 100_000)

    index = 0
    while len(calls) < 600:
        nodes = 2 + index % 80
        values = [rng.randint(1, 1_000_000) for _ in range(nodes)]
        shape = index % 4
        if shape == 0:
            encoded: list[int | None] = values
        elif shape == 1:
            encoded = [values[0]]
            for value in values[1:]:
                encoded.extend((None, value))
        elif shape == 2:
            encoded = [values[0]]
            for value in values[1:]:
                encoded.extend((value, None))
        else:
            encoded = values[:]
            encoded[2] = None
            # Preserve all nodes by appending the omitted value under a later valid parent.
            encoded.extend((values[2], None))
        k = 1 + (index * 7) % nodes
        add(encoded, nodes, k)
        index += 1
    return calls
