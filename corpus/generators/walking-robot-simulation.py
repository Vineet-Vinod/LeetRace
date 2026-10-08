import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        ((4, -1, 3), ()),
        ((4, -1, 4, -2, 4), ((2, 4),)),
        ((6, -1, -1, 6), ((0, 0),)),
    }
    while len(cases) < 600:
        commands = tuple(
            rng.choice((-2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9))
            for _ in range(rng.randint(1, 100))
        )
        obstacles = tuple(
            rng.sample(
                [(x, y) for x in range(-20, 21) for y in range(-20, 21)],
                rng.randint(0, 20),
            )
        )
        cases.add((commands, obstacles))
    return [
        f"candidate(commands={list(commands)!r}, obstacles={[list(point) for point in obstacles]!r})"
        for commands, obstacles in cases
    ]
