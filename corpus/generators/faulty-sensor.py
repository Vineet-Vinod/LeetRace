import random

_STATEMENT_EXAMPLES = (
    "candidate(sensor1=[2, 3, 4, 5], sensor2=[2, 1, 3, 4])",
    "candidate(sensor1=[2, 2, 2, 2, 2], sensor2=[2, 2, 2, 2, 5])",
    "candidate(sensor1=[2, 3, 2, 2, 3, 2], sensor2=[2, 3, 2, 3, 2, 7])",
)


def generate(seed: int = 0) -> list[str]:
    """Generate valid equal-length readings with either one faulty or no sensor."""
    rng = random.Random(seed)
    calls: list[str] = []
    for faulty in (1, 2):
        for _ in range(300):
            length = rng.randint(2, 100)
            normal = [rng.randint(1, 100) for _ in range(length)]
            index = rng.randrange(length)
            replacement = rng.randint(1, 100)
            while replacement == normal[index]:
                replacement = rng.randint(1, 100)
            altered = normal[:index] + normal[index + 1 :] + [replacement]
            first, second = (altered, normal) if faulty == 1 else (normal, altered)
            calls.append(f"candidate(sensor1={first!r}, sensor2={second!r})")
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
