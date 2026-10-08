import random


def generate(seed: int = 0) -> list[str]:
    """Generate decimal strings with no leading zeros, representing nonnegative integers."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        n = 1 + i % 60
        num = str(rng.randrange(1, 10)) + "".join(
            rng.choice("0123456789") for _ in range(n - 1)
        )
        if i % 31 == 0:
            num = "0"
        call = f"candidate(num={num!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
