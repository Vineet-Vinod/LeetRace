import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        (((1, -1, 0), (3, -2, 0)), (1, -1, 0, 1, -1, -1, 3, -2, 0)),
        (((10, -2), (1, 2, 3, 4)), (1, 2, 3, 4, 10, -2)),
        (((1, 2, 3), (3, 4)), (7, 7, 1, 2, 3, 4, 7, 7)),
    }
    cases.add((tuple((value,) for value in range(1000)), tuple(range(1000))))
    cases.add((((10**7,),), (10**7,)))
    while len(cases) < 600:
        if rng.random() < 0.55:
            count = rng.randint(1, 8)
            groups = tuple(
                tuple(rng.randint(-20, 20) for _ in range(rng.randint(1, 6)))
                for _ in range(count)
            )
            chunks = []
            for group in groups:
                chunks.extend(group)
                chunks.extend(rng.randint(-20, 20) for _ in range(rng.randint(0, 2)))
            nums = tuple(chunks)
        else:
            groups = tuple(
                tuple(rng.randint(-20, 20) for _ in range(rng.randint(1, 8)))
                for _ in range(rng.randint(1, 6))
            )
            nums = tuple(rng.randint(-20, 20) for _ in range(rng.randint(1, 45)))
        if sum(map(len, groups)) <= 1000 and len(nums) <= 1000:
            cases.add((groups, nums))
    assert len(cases) == 600 and all(
        1 <= len(g) <= 1000
        and 1 <= len(n) <= 1000
        and 1 <= sum(map(len, g)) <= 1000
        and all(-(10**7) <= v <= 10**7 for x in g for v in x)
        and all(-(10**7) <= v <= 10**7 for v in n)
        for g, n in cases
    )
    return [
        f"candidate(groups={[list(x) for x in g]!r}, nums={list(n)!r})"
        for g, n in sorted(cases)
    ]
