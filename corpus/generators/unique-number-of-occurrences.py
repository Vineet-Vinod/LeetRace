from collections import Counter
import random

_STATEMENT_EXAMPLES = (
    "candidate(arr=[1, 2, 2, 1, 1, 3])",
    "candidate(arr=[1, 2])",
    "candidate(arr=[-3, 0, 1, -3, 1, 1, 1, -3, 10, 0])",
)


def generate(seed: int = 0) -> list[str]:
    """Construct arrays with distinct frequencies and arrays with a collision."""
    rng = random.Random(seed)
    true_cases: set[str] = set()
    false_cases: set[str] = set()
    while len(true_cases) < 300:
        values = rng.sample(range(-1000, 1001), rng.randint(2, 12))
        frequencies = rng.sample(range(1, 25), len(values))
        arr = [value for value, count in zip(values, frequencies) for _ in range(count)]
        rng.shuffle(arr)
        true_cases.add(f"candidate(arr={arr!r})")
    while len(false_cases) < 300:
        values = rng.sample(range(-1000, 1001), rng.randint(2, 12))
        common = rng.randint(1, 15)
        frequencies = [common, common] + rng.sample(range(1, 25), len(values) - 2)
        arr = [value for value, count in zip(values, frequencies) for _ in range(count)]
        rng.shuffle(arr)
        counts = Counter(arr).values()
        if len(counts) != len(set(counts)):
            false_cases.add(f"candidate(arr={arr!r})")
    cases = sorted(true_cases) + sorted(false_cases)
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
