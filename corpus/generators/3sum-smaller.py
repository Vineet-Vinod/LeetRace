def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(nums=[], target=0)", "candidate(nums=[0, 0, 0], target=1)"}
    for _ in range(598):
        size = rng.randint(3, 55)
        nums = [rng.randint(-100, 100) for _ in range(size)]
        target = rng.randint(-100, 100)
        cases.add(f"candidate(nums={nums!r}, target={target})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(nums={[0] * 3500!r}, target=0)"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
