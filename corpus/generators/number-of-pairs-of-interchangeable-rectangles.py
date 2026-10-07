import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    positive = set()
    while len(positive) < 300:
        rectangles = []
        for group in range(1 + rng.randrange(8)):
            width = 1 + rng.randrange(200)
            height = 1 + rng.randrange(200)
            scale = rng.randint(1, 100_000 // max(width, height))
            count = 2 + rng.randrange(8)
            rectangles.extend([[width * scale, height * scale] for _ in range(count)])
        call = f"candidate(rectangles={rectangles!r})"
        positive.add(call)
        calls.add(call)
    for case in range(300):
        count = 2 + case
        rectangles = [[index + 1, 100_000] for index in range(count)]
        calls.add(f"candidate(rectangles={rectangles!r})")
    calls.add(f"candidate(rectangles={[[1, 1] for _ in range(100_000)]!r})")
    calls.add(
        f"candidate(rectangles={[[index, 100_000] for index in range(1, 100_001)]!r})"
    )
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(rectangles=[[4, 5], [7, 8]])",
    "candidate(rectangles=[[4, 8], [3, 6], [10, 20], [15, 30]])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
