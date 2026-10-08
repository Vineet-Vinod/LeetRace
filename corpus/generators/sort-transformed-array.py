import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        nums = sorted(rng.randint(-100, 100) for _ in range(rng.randint(1, 200)))
        a, b, c = (rng.randint(-100, 100) for _ in range(3))
        calls.add(f"candidate(nums={nums!r}, a={a}, b={b}, c={c})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(nums=[-4, -2, 2, 4], a=-1, b=3, c=5)",
    "candidate(nums=[-4, -2, 2, 4], a=1, b=3, c=5)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
