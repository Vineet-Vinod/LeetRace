import random


def generate(seed: int = 0) -> list[str]:
    """Version parts are nonnegative decimal integers separated by dots."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:

        def version():
            return ".".join(str(rng.randrange(10000)) for _ in range(1 + i % 8))

        a = version()
        b = version()
        call = f"candidate(version1={a!r}, version2={b!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
