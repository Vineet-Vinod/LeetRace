import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    for case in range(300):
        groups = 1 + rng.randrange(12)
        tasks = []
        for difficulty in rng.sample(range(1, 10**9), groups):
            tasks.extend([difficulty] * (2 + rng.randrange(50)))
        rng.shuffle(tasks)
        calls.add(f"candidate(tasks={tasks!r})")
    for case in range(300):
        tasks = []
        groups = 1 + rng.randrange(12)
        for difficulty in rng.sample(range(1, 10**9), groups):
            tasks.extend([difficulty] * (2 + rng.randrange(50)))
        used = set(tasks)
        singleton = rng.randint(1, 10**9)
        while singleton in used:
            singleton = rng.randint(1, 10**9)
        tasks.append(singleton)
        rng.shuffle(tasks)
        calls.add(f"candidate(tasks={tasks!r})")
    calls.add(f"candidate(tasks={[7] * 100_000!r})")
    calls.add("candidate(tasks=([7] * 99_999 + [10**9]))")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(tasks=[2, 2, 3, 3, 2, 4, 4, 4, 4, 4])",
    "candidate(tasks=[2, 3, 3])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
