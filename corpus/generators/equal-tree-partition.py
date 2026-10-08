import random


def generate(seed: int = 0) -> list[str]:
    """Mix random trees with trees whose left and right cut sums are equal."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    index = 0

    while len(calls) < 300:
        node_count = 2 + index % 39
        values = [rng.randint(-20, 20) for _ in range(node_count)]
        left_sum = 0
        right_sum = 0
        for node_index in range(1, node_count):
            first_child = node_index
            while first_child > 2:
                first_child = (first_child - 1) // 2
            if first_child == 1:
                left_sum += values[node_index]
            else:
                right_sum += values[node_index]
        values[0] = left_sum - right_sum
        assert -100_000 <= values[0] <= 100_000
        call = f"candidate(root=tree_node({values!r}))"
        index += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for boundary in ([100_000, 100_000], [0] * 10_000):
        call = f"candidate(root=tree_node({boundary!r}))"
        if call not in seen:
            seen.add(call)
            calls.append(call)
    while len(calls) < 600:
        node_count = 1 + index % 40
        values = [rng.randint(-100, 100) for _ in range(node_count)]
        call = f"candidate(root=tree_node({values!r}))"
        index += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
