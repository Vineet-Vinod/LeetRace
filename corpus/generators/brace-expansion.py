import random


def generate(seed: int = 0) -> list[str]:
    """Generate 600 valid expressions of length <= 50 with distinct choices per brace."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    i = 0
    while len(calls) < 600:
        groups = 1 + i % 5
        parts: list[str] = []
        for _ in range(groups):
            choices = rng.sample("abcdef", 1 + rng.randrange(4))
            if len(choices) == 1 and rng.randrange(2):
                parts.append(choices[0])
            else:
                parts.append("{" + ",".join(choices) + "}")
        expression = "".join(parts)
        assert 1 <= len(expression) <= 50
        call = f"candidate(s={expression!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
