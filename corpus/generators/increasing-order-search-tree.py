import random

_STATEMENT_EXAMPLES = (
    "candidate(root=tree_node([5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9]))",
    "candidate(root=tree_node([5, 1, 7]))",
)


def generate(seed: int = 0) -> list[str]:
    """Build valid BST right chains from sorted values, including duplicate values."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        values = sorted(rng.randint(0, 1000) for _ in range(rng.randint(1, 50)))
        level: list[int | None] = []
        for index, value in enumerate(values):
            if index:
                level.append(None)
            level.append(value)
        call = f"candidate(root=tree_node({level!r}))"
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
