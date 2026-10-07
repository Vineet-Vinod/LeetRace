import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        h, w = rng.randint(2, 10**9), rng.randint(2, 10**9)
        hc = sorted(rng.sample(range(1, h), rng.randint(1, min(30, h - 1))))
        vc = sorted(rng.sample(range(1, w), rng.randint(1, min(30, w - 1))))
        calls.add(
            f"candidate(h={h}, w={w}, horizontalCuts={hc!r}, verticalCuts={vc!r})"
        )
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(h=5, w=4, horizontalCuts=[1, 2, 4], verticalCuts=[1, 3])",
    "candidate(h=5, w=4, horizontalCuts=[3], verticalCuts=[3])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
