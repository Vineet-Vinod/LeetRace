import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    calls.add("candidate(tree_node([3, 9, 20, None, None, 15, 7]))")
    while len(calls) < 600:
        size = rng.randint(0, 100)
        values = [rng.randint(-100, 100) for _ in range(size)]
        encoded = []
        for index, value in enumerate(values):
            if index == 0 or rng.random() < 0.82:
                encoded.append(value)
            else:
                encoded.append(None)
        if encoded and encoded[0] is None:
            encoded[0] = 0
        # Remove descendants under absent parents so tree_node receives a valid level-order tree.
        for index in range(1, len(encoded)):
            parent = (index - 1) // 2
            if encoded[parent] is None:
                encoded[index] = None
        while encoded and encoded[-1] is None:
            encoded.pop()
        calls.add(f"candidate(tree_node({encoded!r}))")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = ("candidate(root=tree_node([3, 9, 8, 4, 0, 1, 7]))",)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
