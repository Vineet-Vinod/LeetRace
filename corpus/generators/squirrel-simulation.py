def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        f"candidate(height=100, width=100, tree=[0, 0], squirrel=[99, 99], nuts={[[i % 100, (i * 37) % 100] for i in range(5000)]!r})",
        "candidate(height=5, width=7, tree=[2, 2], squirrel=[4, 4], nuts=[[3, 0], [2, 5]])",
        "candidate(height=1, width=3, tree=[0, 1], squirrel=[0, 0], nuts=[[0, 2]])",
        "candidate(height=100, width=100, tree=[99, 99], squirrel=[0, 0], nuts=[[0, 99], [99, 0]])",
    }
    while len(cases) < 600:
        h, w = rng.randint(1, 100), rng.randint(1, 100)
        tree = [rng.randrange(h), rng.randrange(w)]
        squirrel = [rng.randrange(h), rng.randrange(w)]
        nuts = [[rng.randrange(h), rng.randrange(w)] for _ in range(rng.randint(1, 20))]
        assert 1 <= h <= 100 and 1 <= w <= 100 and 1 <= len(nuts) <= 5000
        assert all(0 <= r < h and 0 <= c < w for r, c in [tree, squirrel, *nuts])
        cases.add(
            f"candidate(height={h}, width={w}, tree={tree!r}, squirrel={squirrel!r}, nuts={nuts!r})"
        )
    return sorted(cases)
