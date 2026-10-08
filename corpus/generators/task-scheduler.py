import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set()
    for i in range(600):
        size = 1 + rng.randrange(160)
        alphabet = string.ascii_uppercase[: 1 + rng.randrange(26)]
        tasks = [rng.choice(alphabet) for _ in range(size)]
        n = rng.randrange(101)
        cases.add(f"candidate(tasks={tasks!r}, n={n})")
    cases.add(f"candidate(tasks={(['A'] * 10_000)!r}, n=100)")
    cases.add(f"candidate(tasks={(['A', 'B'] * 5_000)!r}, n=100)")
    return sorted(cases)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(tasks=['A', 'A', 'A', 'B', 'B', 'B'], n=2)",
    "candidate(tasks=['A', 'C', 'A', 'B', 'D', 'B'], n=1)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))


_AUDIT_BASE_GENERATE = generate
_AUDIT_BOUNDARY_CALLS = ("candidate(tasks=['A'], n=100)",)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_AUDIT_BASE_GENERATE(seed)) | set(_AUDIT_BOUNDARY_CALLS))
