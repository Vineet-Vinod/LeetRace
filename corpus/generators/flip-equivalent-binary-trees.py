import random


def encode_tree(values: list[int | None]) -> list[int | None]:
    if not values:
        return []
    result = []
    queue = [0]
    cursor = 0
    while queue:
        index = queue.pop(0)
        if index >= len(values):
            continue
        value = values[index]
        result.append(value)
        if value is not None:
            queue.extend((index * 2 + 1, index * 2 + 2))
        cursor += 1
    while result and result[-1] is None:
        result.pop()
    return result


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    for case in range(300):
        size = 1 + rng.randrange(80)
        first = rng.sample(range(100), size)
        second = first[:]
        rng.shuffle(second)
        a = [None] * size
        b = [None] * size
        for index, value in enumerate(first):
            a[index] = value
        for index, value in enumerate(second):
            b[index] = value
        first_tree = encode_tree(a)
        second_tree = encode_tree(a if case % 2 == 0 else b)
        calls.add(f"candidate(tree_node({first_tree!r}), tree_node({second_tree!r}))")
    for case in range(300):
        size = 1 + rng.randrange(80)
        first = rng.sample(range(99), size)
        second = rng.sample(range(99, 100), 1)
        a = encode_tree(first)
        b = encode_tree(second)
        calls.add(f"candidate(tree_node({a!r}), tree_node({b!r}))")
    calls.add("candidate(tree_node([]), tree_node([1]))")
    calls.add("candidate(tree_node([0] * 100), tree_node([0] * 100))")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(root1=tree_node([1, 2, 3, 4, 5, 6, None, None, None, 7, 8]), root2=tree_node([1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7]))",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
