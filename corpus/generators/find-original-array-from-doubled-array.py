import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        if rng.random() < 0.5:
            original = [rng.randint(0, 50000) for _ in range(rng.randint(0, 100))]
            changed = original + [2 * x for x in original]
            rng.shuffle(changed)
        else:
            changed = [rng.randint(0, 100000) for _ in range(rng.randint(1, 200))]
        if not changed:
            changed = [0, 0]
        calls.add(f"candidate(changed={changed!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(changed=[1, 3, 4, 2, 6, 8])",
    "candidate(changed=[6, 3, 0, 1])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
