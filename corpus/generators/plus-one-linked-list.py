import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        size = rng.randint(1, 100)
        digits = [rng.randint(0, 9) for _ in range(size)]
        if size > 1 and digits[0] == 0:
            digits[0] = rng.randint(1, 9)
        calls.add(f"candidate(list_node({digits!r}))")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(head=list_node([1, 2, 3]))",
    "candidate(head=list_node([9, 9]))",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
