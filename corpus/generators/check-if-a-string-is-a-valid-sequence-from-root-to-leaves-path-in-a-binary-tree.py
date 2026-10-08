import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    calls.add(
        "candidate(tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0]), arr=[0, 1, 0, 1])"
    )
    while len(calls) < 600:
        size = rng.randint(1, 45)
        values = [rng.randint(0, 9) for _ in range(size)]
        encoded: list[int | None] = values[:]
        for index in range(1, size):
            if encoded[(index - 1) // 2] is None:
                encoded[index] = None
        while encoded and encoded[-1] is None:
            encoded.pop()
        arr = [rng.randint(0, 9) for _ in range(rng.randint(1, 50))]
        if rng.random() < 0.5:
            path = []
            node = 0
            while node < len(encoded) and encoded[node] is not None:
                path.append(encoded[node])
                children = [
                    i
                    for i in (node * 2 + 1, node * 2 + 2)
                    if i < len(encoded) and encoded[i] is not None
                ]
                if not children:
                    break
                node = rng.choice(children)
            if path:
                arr = path
        calls.add(f"candidate(tree_node({encoded!r}), arr={arr!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(root=tree_node([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0]), arr=[0, 1, 1])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
