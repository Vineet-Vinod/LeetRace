import random

EXAMPLES = [
    "candidate(fruits=[[2, 8], [6, 3], [8, 6]], startPos=5, k=4)",
    "candidate(fruits=[[0, 9], [4, 1], [5, 7], [6, 2], [7, 4], [10, 9]], startPos=5, k=4)",
    "candidate(fruits=[[0, 3], [6, 4], [8, 5]], startPos=3, k=2)",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = list(EXAMPLES)
    seen = set(calls)

    def emit(call: str) -> None:
        if call not in seen:
            calls.append(call)
            seen.add(call)

    def add(fruits, start, k):
        assert 1 <= len(fruits) <= 100000 and 0 <= start <= 200000 and 0 <= k <= 200000
        assert all(
            len(p) == 2 and 0 <= p[0] <= 200000 and 1 <= p[1] <= 10000 for p in fruits
        )
        assert all(a[0] < b[0] for a, b in zip(fruits, fruits[1:]))
        emit(f"candidate(fruits={fruits!r}, startPos={start}, k={k})")

    add([[2 * i, 10000] for i in range(100000)], 100000, 200000)
    add([[200000, 10000]], 200000, 0)
    add([[200000, 10000]], 0, 0)
    add([[0, 1]], 0, 0)
    while len(calls) < 600:
        positions = sorted(rng.sample(range(201), rng.randint(1, 35)))
        fruits = [[p, rng.randint(1, 10000)] for p in positions]
        start = rng.randint(0, 200)
        k = rng.choice([0, 1, rng.randint(1, 200)])
        add(fruits, start, k)
    return calls
