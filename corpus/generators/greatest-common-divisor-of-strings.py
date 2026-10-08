import random
import string

_STATEMENT_EXAMPLES = (
    "candidate(str1='ABCABC', str2='ABC')",
    "candidate(str1='ABABAB', str2='ABAB')",
    "candidate(str1='LEET', str2='CODE')",
)


def generate(seed: int = 0) -> list[str]:
    """Generate distinct uppercase strings, often as repetitions of shared bases."""
    rng = random.Random(seed)
    calls = [f"candidate(str1={'A' * 1000!r}, str2={'A' * 999!r})"]
    seen = set(calls)
    while len(calls) < 600:
        base = "".join(
            rng.choice(string.ascii_uppercase) for _ in range(rng.randint(1, 10))
        )
        if rng.randrange(2):
            first = base * rng.randint(1, 20)
            second = base * rng.randint(1, 20)
        else:
            first = "".join(
                rng.choice(string.ascii_uppercase) for _ in range(rng.randint(1, 30))
            )
            second = "".join(
                rng.choice(string.ascii_uppercase) for _ in range(rng.randint(1, 30))
            )
        call = f"candidate(str1={first!r}, str2={second!r})"
        if len(first) <= 1000 and len(second) <= 1000 and call not in seen:
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
