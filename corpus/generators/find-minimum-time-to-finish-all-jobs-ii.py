import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: equal nonempty lengths up to 10^5; values1..10^5."""
    rng = random.Random(seed)
    calls = {
        "candidate(jobs=[5, 2, 4], workers=[1, 7, 5])",
        "candidate(jobs=[3, 18, 15, 9], workers=[6, 5, 1, 3])",
        "candidate(jobs=list(range(1, 100001)), workers=[100000] * 100000)",
        "candidate(jobs=[100000] * 100000, workers=list(range(1, 100001)))",
    }
    while len(calls) < 600:
        size = rng.randint(1, 200)
        jobs = [rng.randint(1, 100_000) for _ in range(size)]
        workers = [rng.randint(1, 100_000) for _ in range(size)]
        assert 1 <= len(jobs) == len(workers) <= 100_000
        assert all(1 <= value <= 100_000 for value in jobs + workers)
        calls.add(f"candidate(jobs={jobs!r}, workers={workers!r})")
    return sorted(calls)
