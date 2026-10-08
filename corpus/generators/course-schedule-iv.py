import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        n = rng.randint(2, 50)
        order = list(range(n))
        rng.shuffle(order)
        rank = {course: index for index, course in enumerate(order)}
        edges = [
            [a, b]
            for a in range(n)
            for b in range(n)
            if rank[a] < rank[b] and rng.random() < 0.06
        ]
        queries = []
        for _ in range(rng.randint(1, 100)):
            u, v = rng.sample(range(n), 2)
            queries.append([u, v])
        calls.add(
            f"candidate(numCourses={n}, prerequisites={edges!r}, queries={queries!r})"
        )
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(numCourses=2, prerequisites=[[1, 0]], queries=[[0, 1], [1, 0]])",
    "candidate(numCourses=3, prerequisites=[[1, 2], [1, 0], [2, 0]], queries=[[1, 0], [1, 2]])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
