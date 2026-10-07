import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(intervals: list[list[int]], queries: list[int]) -> None:
        assert 1 <= len(intervals) <= 100000 and 1 <= len(queries) <= 100000
        assert all(
            len(x) == 2 and 1 <= x[0] <= x[1] <= 10**7 for x in intervals
        ) and all(1 <= x <= 10**7 for x in queries)
        call = (
            "candidate("
            + ", ".join(
                f"{key}={value!r}"
                for key, value in [("intervals", intervals), ("queries", queries)]
            )
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(intervals=[[1, 4], [2, 4], [3, 6], [4, 4]], queries=[2, 3, 4, 5])
    add(intervals=[[i, i] for i in range(1, 100001)], queries=list(range(1, 100001)))
    add(intervals=[[1, 10**7]], queries=[1, 10**7, 5000000])
    add(intervals=[[1, 4], [2, 4], [3, 6], [4, 4]], queries=[2, 3, 4, 5])
    add(intervals=[[2, 3], [2, 5], [1, 8], [20, 25]], queries=[2, 19, 5, 22])
    while len(calls) < 600:
        intervals = []
        for _ in range(rng.randint(1, 25)):
            a = rng.randint(1, 100)
            intervals.append([a, a + rng.randint(0, 50)])
        queries = [rng.randint(1, 180) for _ in range(rng.randint(1, 35))]
        add(intervals=intervals, queries=queries)
    return calls
