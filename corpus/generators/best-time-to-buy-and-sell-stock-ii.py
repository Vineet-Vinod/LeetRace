import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    up_down = tuple(range(10001)) + tuple(reversed(range(10001))) + (0,) * 9998
    arrays = {
        (0,),
        up_down,
        tuple(reversed(range(10001))) + (10000,) * 19999,
        (10000,) * 30000,
    }
    while len(arrays) < 600:
        values = tuple(rng.randint(0, 10000) for _ in range(rng.randint(1, 100)))
        arrays.add(values)
    cases = [f"candidate(prices={list(values)!r})" for values in arrays]
    assert len(cases) == len(set(cases)) == 600
    assert all(
        1 <= len(values) <= 30000 and all(0 <= value <= 10000 for value in values)
        for values in arrays
    )
    assert any(len(values) == 30000 for values in arrays)
    return cases
