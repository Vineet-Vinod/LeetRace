import random

_STATEMENT_EXAMPLES = (
    "candidate(n=2, trust=[[1, 2]])",
    "candidate(n=3, trust=[[1, 3], [2, 3]])",
    "candidate(n=3, trust=[[1, 3], [2, 3], [3, 1]])",
)


def generate(seed: int = 0) -> list[str]:
    """Construct distinct judge graphs and graphs with no qualifying judge."""
    rng = random.Random(seed)
    judge_cases: set[str] = set()
    while len(judge_cases) < 300:
        n = rng.randint(2, 100)
        judge = rng.randint(1, n)
        trust = [[person, judge] for person in range(1, n + 1) if person != judge]
        rng.shuffle(trust)
        judge_cases.add(f"candidate(n={n}, trust={trust!r})")
    no_judge_cases = [
        f"candidate(n={n}, trust={([[1, 2]] if n > 2 else [])!r})"
        for n in range(2, 302)
    ]
    cases = list(judge_cases) + no_judge_cases
    rng.shuffle(cases)
    return cases


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
