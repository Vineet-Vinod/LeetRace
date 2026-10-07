import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(startTime: list[int], endTime: list[int], profit: list[int]) -> None:
        assert 1 <= len(startTime) == len(endTime) == len(profit) <= 50000
        assert all(
            1 <= a < b <= 10**9 and 1 <= p <= 10000
            for a, b, p in zip(startTime, endTime, profit)
        )
        call = (
            "candidate("
            + ", ".join(
                f"{key}={value!r}"
                for key, value in [
                    ("startTime", startTime),
                    ("endTime", endTime),
                    ("profit", profit),
                ]
            )
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(startTime=[1, 2, 3, 3], endTime=[3, 4, 5, 6], profit=[50, 10, 40, 70])
    add(
        startTime=list(range(1, 50001)),
        endTime=list(range(2, 50002)),
        profit=[10000] * 50000,
    )
    add(startTime=[1] * 50000, endTime=[10**9] * 50000, profit=[1] * 49999 + [10000])
    add(startTime=[1, 2, 3, 3], endTime=[3, 4, 5, 6], profit=[50, 10, 40, 70])
    add(
        startTime=[1, 2, 3, 4, 6],
        endTime=[3, 5, 10, 6, 9],
        profit=[20, 20, 100, 70, 60],
    )
    add(startTime=[1, 1, 1], endTime=[2, 3, 4], profit=[5, 6, 4])
    while len(calls) < 600:
        n = rng.randint(1, 35)
        starts = [rng.randint(1, 100) for _ in range(n)]
        ends = [x + rng.randint(1, 50) for x in starts]
        profits = [rng.randint(1, 10000) for _ in starts]
        add(startTime=starts, endTime=ends, profit=profits)
    return calls
