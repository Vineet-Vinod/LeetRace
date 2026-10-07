import random

_STATEMENT_EXAMPLES = ("candidate(nums=[3, 6, 1, 0])", "candidate(nums=[1, 2, 3, 4])")


def generate(seed: int = 0) -> list[str]:
    """Construct unique maxima both above and below the required doubling threshold."""
    rng = random.Random(seed)
    true_cases: list[str] = []
    false_cases: list[str] = []
    for maximum in range(2, 101):
        for runner_up in range(0, maximum // 2 + 1):
            true_cases.append(f"candidate(nums={[maximum, runner_up]!r})")
        for runner_up in range(maximum // 2 + 1, maximum):
            false_cases.append(f"candidate(nums={[maximum, runner_up]!r})")
    rng.shuffle(true_cases)
    rng.shuffle(false_cases)
    return true_cases[:300] + false_cases[:300]


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
