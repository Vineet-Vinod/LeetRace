import random

EXAMPLES = [
    "candidate(intervals=[[1, 3], [3, 7], [8, 9]])",
    "candidate(intervals=[[1, 3], [1, 4], [2, 5], [3, 5]])",
    "candidate(intervals=[[1, 2], [2, 3], [2, 4], [4, 5]])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = list(EXAMPLES)
    seen = set(calls)

    def emit(call: str) -> None:
        if call not in seen:
            calls.append(call)
            seen.add(call)

    def add(intervals):
        assert 1 <= len(intervals) <= 3000
        assert all(len(p) == 2 and 0 <= p[0] < p[1] <= 10**8 for p in intervals)
        emit(f"candidate(intervals={intervals!r})")

    add([[2 * i, 2 * i + 1] for i in range(3000)])
    add([[0, 10**8]] * 3000)
    while len(calls) < 600:
        intervals = []
        for _ in range(rng.randint(1, 35)):
            a = rng.randint(0, 100)
            intervals.append([a, a + rng.randint(1, 80)])
        add(intervals)
    return calls
