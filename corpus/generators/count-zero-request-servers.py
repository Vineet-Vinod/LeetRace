import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: n/logs/queries up to 100000; x<each query; includes boundary log and query counts."""
    rng = random.Random(seed)
    calls = {
        "candidate(n=3, logs=[[1, 3], [2, 6], [1, 5]], x=5, queries=[10, 11])",
        f"candidate(n=100000, logs={[[server, server] for server in range(1, 100001)]!r}, x=10, queries={[100000, 100001, 99999]!r})",
    }
    while len(calls) < 600:
        n = rng.randint(1, 30)
        log_count = rng.randint(1, 80)
        logs = [[rng.randint(1, n), rng.randint(1, 1000)] for _ in range(log_count)]
        x = rng.randint(1, 100)
        queries = [rng.randint(x + 1, 1000) for _ in range(rng.randint(1, 30))]
        calls.add(f"candidate(n={n}, logs={logs!r}, x={x}, queries={queries!r})")
    return sorted(calls)
