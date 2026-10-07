import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, int, int, int]] = {
        (1, 2, 1, 600),
        (0, 1, 2, 76),
        (0, 1, 1, 1),
        (9, 10**5, 10**5, 6039),
    }
    while len(cases) < 600:
        cases.add(
            (
                rng.randint(0, 9),
                rng.randint(1, 10**5),
                rng.randint(1, 10**5),
                rng.randint(1, 6039),
            )
        )
    assert all(
        0 <= start <= 9
        and 1 <= move <= 10**5
        and 1 <= push <= 10**5
        and 1 <= target <= 6039
        for start, move, push, target in cases
    )
    return [
        f"candidate(startAt={start}, moveCost={move}, pushCost={push}, targetSeconds={target})"
        for start, move, push, target in sorted(cases)
    ]
