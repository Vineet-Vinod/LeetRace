def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        pair_count = rng.randint(1, 40)
        target = rng.randint(2, 1001)
        skill = []
        for _ in range(pair_count):
            first = rng.randint(1, target - 1)
            skill.extend((first, target - first))
        rng.shuffle(skill)
        if rng.random() < 0.4:
            skill[-1] = rng.randint(1, 1000)
        assert len(skill) % 2 == 0 and all(1 <= value <= 1000 for value in skill)
        cases.add(f"candidate(skill={skill!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(skill={[1] * 100000!r})"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
