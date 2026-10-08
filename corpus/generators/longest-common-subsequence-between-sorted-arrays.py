def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    common = [list(range(1, 101)) for _ in range(100)]
    disjoint = [[value] for value in range(1, 101)]
    possible = {f"candidate(arrays={common!r})"}
    impossible = {f"candidate(arrays={disjoint!r})"}
    while len(possible) < 300:
        count = rng.randint(2, 8)
        shared = sorted(rng.sample(range(1, 101), rng.randint(1, 10)))
        arrays = []
        for _ in range(count):
            extras = rng.sample(
                [value for value in range(1, 101) if value not in shared],
                rng.randint(0, 20),
            )
            arrays.append(sorted(shared + extras))
        assert 2 <= len(arrays) <= 100
        assert all(1 <= len(row) <= 100 and row == sorted(set(row)) for row in arrays)
        possible.add(f"candidate(arrays={arrays!r})")
    while len(impossible) < 300:
        count = rng.randint(2, 8)
        values = rng.sample(range(1, 101), count)
        arrays = [[value] for value in values]
        assert len(set(values)) == len(values)
        impossible.add(f"candidate(arrays={arrays!r})")
    return sorted(possible | impossible)
