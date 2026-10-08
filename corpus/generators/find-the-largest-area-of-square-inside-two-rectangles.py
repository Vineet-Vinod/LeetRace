import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    for case in range(300):
        n = 2 + rng.randrange(20)
        x, y = rng.randint(101, 9_999_000), rng.randint(101, 9_999_000)
        width, height = rng.randint(1, 100), rng.randint(1, 100)
        bottom, top = [], []
        for _ in range(n):
            bottom.append([x - rng.randint(0, 100), y - rng.randint(0, 100)])
            top.append(
                [x + width + rng.randint(0, 100), y + height + rng.randint(0, 100)]
            )
        calls.add(f"candidate(bottomLeft={bottom!r}, topRight={top!r})")
    for case in range(300):
        n = 2 + rng.randrange(20)
        bottom, top = [], []
        for index in range(n):
            x = 1 + index * 102
            width = 1 + rng.randrange(100)
            y = rng.randint(1, 10**7 - 100)
            height = 1 + rng.randrange(100)
            bottom.append([x, y])
            top.append([x + width, y + height])
        calls.add(f"candidate(bottomLeft={bottom!r}, topRight={top!r})")
    # Maximum rectangle count and coordinate boundary with a common 10^7-wide square.
    bottom = [[1, 1] for _ in range(1000)]
    top = [[10**7, 10**7] for _ in range(1000)]
    calls.add(f"candidate(bottomLeft={bottom!r}, topRight={top!r})")
    bottom = [[index * 100 + 1, 1] for index in range(1000)]
    top = [[index * 100 + 50, 50] for index in range(1000)]
    calls.add(f"candidate(bottomLeft={bottom!r}, topRight={top!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(bottomLeft=[[1, 1], [2, 2], [3, 1]], topRight=[[3, 3], [4, 4], [6, 6]])",
    "candidate(bottomLeft=[[1, 1], [3, 3], [3, 1]], topRight=[[2, 2], [4, 4], [4, 2]])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
