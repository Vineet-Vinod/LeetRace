import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        n, users = rng.randint(2, 50), rng.randint(1, 50)
        languages = []
        for _ in range(users):
            known = rng.sample(range(1, n + 1), rng.randint(1, n))
            languages.append(known)
        pairs = [(a, b) for a in range(1, users + 1) for b in range(a + 1, users + 1)]
        rng.shuffle(pairs)
        friendships = (
            [list(pair) for pair in pairs[: rng.randint(1, len(pairs))]]
            if pairs
            else []
        )
        if not friendships:
            if users == 1:
                continue
            friendships = [[1, 2]]
        calls.add(
            f"candidate(n={n}, languages={languages!r}, friendships={friendships!r})"
        )
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(n=2, languages=[[1], [2], [1, 2]], friendships=[[1, 2], [1, 3], [2, 3]])",
    "candidate(n=3, languages=[[2], [1, 3], [1, 2], [3]], friendships=[[1, 4], [1, 2], [3, 4], [2, 3]])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
