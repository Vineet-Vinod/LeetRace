def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        nums = [rng.randint(0, 100000) for _ in range(rng.randint(1, 100))]
        k = rng.randint(0, 100000)
        cases.add(f"candidate(nums={nums!r}, k={k})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(nums={[1] * 100000!r}, k=100000)"
    if boundary not in calls:
        calls[-1] = boundary

    def validate(nums: list[int], k: int) -> None:
        assert 1 <= len(nums) <= 100_000
        assert all(0 <= value <= 100_000 for value in nums)
        assert 0 <= k <= 100_000

    for call in calls:
        eval(call, {"candidate": validate})
    assert 500 <= len(calls) <= 999 and len(calls) == len(set(calls))
    return sorted(calls)
