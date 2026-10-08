def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        arrays = []
        total = 0
        for _ in range(rng.randint(2, 20)):
            if total >= 100:
                break
            row = sorted(
                rng.randint(-10000, 10000)
                for _ in range(rng.randint(1, min(20, 100 - total)))
            )
            arrays.append(row)
            total += len(row)
        assert (
            len(arrays) >= 2
            and all(row == sorted(row) for row in arrays)
            and total <= 100000
        )
        cases.add(f"candidate(arrays={arrays!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(arrays={[[(-10000 if index % 2 == 0 else 10000)] for index in range(100000)]!r})"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
