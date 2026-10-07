import random

_STATEMENT_EXAMPLES = (
    "candidate(root=tree_node([1, None, 2, 2]))",
    "candidate(root=tree_node([0]))",
)


def generate(seed: int = 0) -> list[str]:
    """Create distinct valid BSTs as level-order right chains; duplicate keys go right."""
    rng = random.Random(seed)
    boundary = [0]
    for _ in range(9999):
        boundary.extend((None, 0))
    calls = [f"candidate(root=tree_node({boundary!r}))"]
    seen = set(calls)
    while len(calls) < 600:
        values = sorted(rng.randint(-10000, 10000) for _ in range(rng.randint(1, 50)))
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
