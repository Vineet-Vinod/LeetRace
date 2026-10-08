import random

EXAMPLES = [
    "candidate(arr=[6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12], d=2)",
    "candidate(arr=[3, 3, 3, 3, 3], d=3)",
    "candidate(arr=[7, 6, 5, 4, 3, 2, 1], d=1)",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = list(EXAMPLES)
    seen = set(calls)

    def emit(call: str) -> None:
        if call not in seen:
            calls.append(call)
            seen.add(call)

    def add(arr, d):
        assert 1 <= len(arr) <= 1000 and 1 <= d <= len(arr)
        assert all(1 <= v <= 100000 for v in arr)
        emit(f"candidate(arr={arr!r}, d={d})")

    add(list(range(1000, 0, -1)), 1000)
    add([100000] * 1000, 1000)
    add([1], 1)
    while len(calls) < 600:
        n = rng.randint(1, 50)
        arr = [rng.randint(1, 100000) for _ in range(n)]
        if rng.random() < 0.25:
            arr = [rng.randint(1, 5) for _ in range(n)]
        if rng.random() < 0.25:
            arr.sort(reverse=True)
        add(arr, rng.randint(1, n))
    return calls
