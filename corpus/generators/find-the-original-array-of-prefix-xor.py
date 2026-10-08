import random


_MAX_LENGTH = 100_000
_MAX_PREFIX = 1_000_000


def generate(seed: int = 0) -> list[str]:
    """Build prefix arrays directly so every pref[i] stays within [0, 10^6]."""
    rng = random.Random(seed)
    cases = {
        (5, 2, 0, 3, 1),
        (13,),
        (0,),
        (_MAX_PREFIX,),
        tuple([0] * _MAX_LENGTH),
        tuple([0, _MAX_PREFIX] * (_MAX_LENGTH // 2)),
    }
    while len(cases) < 600:
        length = rng.randint(1, 1000)
        prefixes = tuple(rng.randint(0, _MAX_PREFIX) for _ in range(length))
        cases.add(prefixes)
    assert len(cases) == 600
    assert all(1 <= len(prefixes) <= _MAX_LENGTH for prefixes in cases)
    assert all(0 <= value <= _MAX_PREFIX for prefixes in cases for value in prefixes)
    return [f"candidate(pref={list(prefixes)!r})" for prefixes in sorted(cases)]
