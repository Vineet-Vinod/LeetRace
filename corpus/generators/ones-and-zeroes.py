import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        strs = [
            "".join(rng.choice("01") for _ in range(rng.randint(1, 20)))
            for _ in range(rng.randint(1, 100))
        ]
        m, n = rng.randint(1, 100), rng.randint(1, 100)
        calls.add(f"candidate(strs={strs!r}, m={m}, n={n})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(strs=['10', '0', '1'], m=1, n=1)",
    "candidate(strs=['10', '0001', '111001', '1', '0'], m=5, n=3)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
