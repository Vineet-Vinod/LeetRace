import random


def generate(seed: int = 0) -> list[str]:
    """Even length arrays with bounded integers and positive k."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        n = 2 * (1 + i % 20)
        k = 1 + (i * 7) % 25
        arr = [rng.randrange(-100, 101) for _ in range(n)]
        assert (
            len(arr) % 2 == 0
            and 1 <= k <= 10**5
            and all(-(10**9) <= x <= 10**9 for x in arr)
        )
        call = f"candidate(arr={arr!r}, k={k})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
