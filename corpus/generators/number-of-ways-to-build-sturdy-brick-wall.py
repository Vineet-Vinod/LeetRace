import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(2, 3, (1, 2)), (1, 1, (5,))}
    while len(cases) < 600:
        width = rng.randint(1, 10)
        bricks = tuple(sorted(rng.sample(range(1, 11), rng.randint(1, 10))))
        cases.add((rng.randint(1, 100), width, bricks))
    return [
        f"candidate(height={height}, width={width}, bricks={list(bricks)!r})"
        for height, width, bricks in cases
    ]
