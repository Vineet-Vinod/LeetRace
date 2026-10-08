_STATEMENT_EXAMPLES = ("candidate(n=4)", "candidate(n=25)")
DOMAIN_SIZE = 38


def generate(seed: int = 0) -> list[str]:
    """The complete legal scalar domain is the 38 integers from 0 through 37."""
    return [f"candidate(n={n})" for n in range(38)]


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
