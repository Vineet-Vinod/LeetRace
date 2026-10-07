import random

EXAMPLES = [
    "candidate(n=3, x=1, y=3)",
    "candidate(n=5, x=2, y=4)",
    "candidate(n=4, x=1, y=1)",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = list(EXAMPLES)
    seen = set(calls)

    def emit(call: str) -> None:
        if call not in seen:
            calls.append(call)
            seen.add(call)

    def add(n, x, y):
        assert 2 <= n <= 100000 and 1 <= x <= n and 1 <= y <= n
        emit(f"candidate(n={n}, x={x}, y={y})")

    add(100000, 1, 100000)
    add(100000, 50000, 50000)
    add(100000, 25000, 75000)
    for n in range(2, 12):
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                if len(calls) < 520:
                    add(n, x, y)
    while len(calls) < 600:
        n = rng.randint(12, 300)
        add(n, rng.randint(1, n), rng.randint(1, n))
    return calls
