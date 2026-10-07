import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    calls.add("candidate(tree_node([1, 2, 3, 4, 5, 6, 7]))")
    while len(calls) < 600:
        size = rng.randint(1, 100)
        encoded = [rng.randint(-1000, 1000)]
        for index in range(1, size):
            parent = rng.randrange(index)
            # The encoding is assembled as a connected tree using a free child slot.
            while True:
                slot = parent * 2 + rng.choice((1, 2))
                if slot >= len(encoded):
                    encoded.extend([None] * (slot + 1 - len(encoded)))
                if encoded[slot] is None:
                    encoded[slot] = rng.randint(-1000, 1000)
                    break
                parent = rng.randrange(index)
        while encoded and encoded[-1] is None:
            encoded.pop()
        calls.add(f"candidate(tree_node({encoded!r}))")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(root=tree_node([1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10]))",
    "candidate(root=tree_node([1, None, 2, 3, 4]))",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
