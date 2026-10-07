def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        nums = [rng.randint(1, 100) for _ in range(rng.randint(1, 100))]
        prime_index = rng.randrange(len(nums))
        nums[prime_index] = rng.choice(
            [
                2,
                3,
                5,
                7,
                11,
                13,
                17,
                19,
                23,
                29,
                31,
                37,
                41,
                43,
                47,
                53,
                59,
                61,
                67,
                71,
                73,
                79,
                83,
                89,
                97,
            ]
        )
        assert any(
            value
            in {
                2,
                3,
                5,
                7,
                11,
                13,
                17,
                19,
                23,
                29,
                31,
                37,
                41,
                43,
                47,
                53,
                59,
                61,
                67,
                71,
                73,
                79,
                83,
                89,
                97,
            }
            for value in nums
        )
        cases.add(f"candidate(nums={nums!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(nums={[2] + [4] * 299998 + [97]!r})"
    if boundary not in calls:
        calls[-1] = boundary

    def validate(nums: list[int]) -> None:
        assert 1 <= len(nums) <= 300_000
        assert all(1 <= value <= 100 for value in nums)
        assert any(
            value
            in {
                2,
                3,
                5,
                7,
                11,
                13,
                17,
                19,
                23,
                29,
                31,
                37,
                41,
                43,
                47,
                53,
                59,
                61,
                67,
                71,
                73,
                79,
                83,
                89,
                97,
            }
            for value in nums
        )

    for call in calls:
        eval(call, {"candidate": validate})
    assert 500 <= len(calls) <= 999
    return calls
