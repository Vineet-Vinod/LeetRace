import random

_STATEMENT_EXAMPLES = (
    "candidate(root=tree_node([1, 0, 1, 0, 1, 0, 1]))",
    "candidate(root=tree_node([0]))",
)


def generate(seed: int = 0) -> list[str]:
    """Generate nonempty complete binary trees with 0/1 node values, at most 1000 nodes."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        size = 1000 if len(calls) == 0 else rng.randint(1, 100)
        values = [rng.randrange(2) for _ in range(size)]
        call = f"candidate(root=tree_node({values!r}))"
        if call not in seen:
            calls.append(call)
            seen.add(call)
    return calls


_BASE_GENERATE = generate


def generate(seed: int = 0) -> list[str]:
    calls = list(_STATEMENT_EXAMPLES)
    seen = set(calls)
    for call in _BASE_GENERATE(seed):
        if call not in seen:
            calls.append(call)
            seen.add(call)
    limit = globals().get("DOMAIN_SIZE", 600)
    if len(calls) < limit:
        raise ValueError("Generator did not produce enough distinct cases")
    return calls[:limit]
