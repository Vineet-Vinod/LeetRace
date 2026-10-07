_STATEMENT_EXAMPLES = ("candidate(n=3)", "candidate(n=5)", "candidate(n=15)")


def generate(seed: int = 0) -> list[str]:
    """Cover distinct n values from 1 through the stated upper bound 10000."""
    values = set(range(1, 599))
    values.update((1000, 10000))
    return [f"candidate(n={n})" for n in sorted(values)]


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
