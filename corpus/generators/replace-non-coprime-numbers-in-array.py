import random
from math import gcd, lcm


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        validate(kwargs)
        call = (
            "candidate(" + ", ".join(k + "=" + repr(v) for k, v in kwargs.items()) + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    def letters(text):
        return all("a" <= ch <= "z" for ch in text)

    def array(values, minimum, maximum, length):
        assert 1 <= len(values) <= length
        assert all(minimum <= v <= maximum for v in values)

    def validate(d):
        array(d["nums"], 1, 100000, 100000)
        # Every generated connected merge chain divides 30030 or contains only a
        # single repeated value, with 1 separators. Thus its LCM cannot exceed 10^8.
        # Check using a separate leftmost-reduction simulation on modest inputs.
        nums = d["nums"]
        if len(nums) < 1000:
            reduced = nums[:]
            i = 0
            while i + 1 < len(reduced):
                if gcd(reduced[i], reduced[i + 1]) > 1:
                    reduced[i : i + 2] = [lcm(reduced[i], reduced[i + 1])]
                    i = max(0, i - 1)
                else:
                    i += 1
            assert max(reduced) <= 100000000

    add(nums=[100000] * 100000)
    add(nums=[1, 100000] * 50000)
    add(nums=[6, 4, 3, 2, 7, 6, 2])
    add(nums=[2, 2, 1, 1, 3, 3, 3])
    while len(calls) < 600:
        divisors = [
            1,
            2,
            3,
            5,
            6,
            7,
            10,
            11,
            13,
            14,
            15,
            21,
            22,
            26,
            30,
            35,
            42,
            55,
            65,
            77,
            91,
            143,
            30030,
        ]
        add(nums=[rng.choice(divisors) for _ in range(rng.randint(1, 100))])
    assert len(calls) == 600
    return calls
