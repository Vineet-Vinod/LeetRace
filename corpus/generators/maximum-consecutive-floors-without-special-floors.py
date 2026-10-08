import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, int, tuple[int, ...]]] = {
        (2, 9, (4, 6)),
        (6, 8, (6, 7, 8)),
        (1, 10**9, (1, 10**9)),
        (100, 100, (100,)),
    }
    cases.add((1, 10**9, tuple(range(1, 100_001))))
    while len(cases) < 600:
        bottom = rng.randint(1, 10**9 - 100)
        top = bottom + rng.randint(0, 100)
        special = tuple(
            sorted(rng.sample(range(bottom, top + 1), rng.randint(1, top - bottom + 1)))
        )
        cases.add((bottom, top, special))
    assert all(
        1 <= bottom <= top <= 10**9
        and 1 <= len(special) <= 100_000
        and len(set(special)) == len(special)
        and all(bottom <= floor <= top for floor in special)
        for bottom, top, special in cases
    )
    return [
        f"candidate(bottom={bottom}, top={top}, special={list(special)!r})"
        for bottom, top, special in sorted(cases)
    ]
