import random


def generate(seed: int = 0) -> list[str]:
    """Inputs are digit strings with no leading zeros, bounded at 10,000 digits."""
    rng = random.Random(seed)
    cases = [("0", "0"), ("1", "9"), ("999", "1"), ("9" * 10000, "1")]
    seen = set(cases)
    while len(cases) < 600:
        a_len = rng.randint(1, 120)
        b_len = rng.randint(1, 120)
        a = str(rng.randint(1, 9)) + "".join(
            str(rng.randrange(10)) for _ in range(a_len - 1)
        )
        b = str(rng.randint(1, 9)) + "".join(
            str(rng.randrange(10)) for _ in range(b_len - 1)
        )
        if a_len == 1 and rng.randrange(4) == 0:
            a = "0"
        pair = (a, b)
        if pair not in seen:
            seen.add(pair)
            cases.append(pair)
    return [f"candidate(num1={a!r}, num2={b!r})" for a, b in cases]


_EXAMPLE_CALLS = [
    "candidate(num1='11', num2='123')",
    "candidate(num1='456', num2='77')",
]

_PREVIOUS_GENERATE = generate


def generate(seed: int = 0) -> list[str]:
    calls = _PREVIOUS_GENERATE(seed)
    return calls + [call for call in _EXAMPLE_CALLS if call not in calls]
