import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    positive = set()
    while len(positive) < 300:
        size = 2 + rng.randrange(300)
        target = 1 + rng.randrange(6)
        tops, bottoms = [], []
        for _ in range(size):
            if rng.randrange(2):
                tops.append(target)
                bottoms.append(rng.randint(1, 6))
            else:
                tops.append(rng.randint(1, 6))
                bottoms.append(target)
        call = f"candidate(tops={tops!r}, bottoms={bottoms!r})"
        positive.add(call)
        calls.add(call)
    for case in range(300):
        size = 2 + case
        tops = [1 + (index % 3) for index in range(size)]
        bottoms = [4 + (index % 3) for index in range(size)]
        calls.add(f"candidate(tops={tops!r}, bottoms={bottoms!r})")
    calls.add("candidate(tops=[1] * 20000, bottoms=[2] * 20000)")
    calls.add("candidate(tops=[1, 2] * 10000, bottoms=[2, 1] * 10000)")
    calls.add("candidate(tops=[6, 1] * 10000, bottoms=[2, 6] * 10000)")
    calls.add(
        "candidate(tops=([2] * 5000 + [1] * 15000), bottoms=([1] * 5000 + [2] * 15000))"
    )
    calls.add("candidate(tops=([1] * 19999 + [3]), bottoms=([2] * 19999 + [4]))")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(tops=[2, 1, 2, 4, 2, 2], bottoms=[5, 2, 6, 2, 3, 2])",
    "candidate(tops=[3, 5, 1, 2, 3], bottoms=[3, 6, 3, 3, 4])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
