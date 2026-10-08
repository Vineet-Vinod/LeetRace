import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        s = "".join(rng.choice("01") for _ in range(rng.randint(1, 1000)))
        k = rng.randint(1, 10**9)
        calls.add(f"candidate(s={s!r}, k={k})")
    calls.add(f"candidate(s={'01' * 500!r}, k=1000000000)")
    calls.add(f"candidate(s={'1' * 1_000!r}, k=1)")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(s='00101001', k=1)",
    "candidate(s='1001010', k=5)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
