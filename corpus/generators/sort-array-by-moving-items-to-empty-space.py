import random
from itertools import permutations


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        calls[
            "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        ] = None

    add(nums=list(range(100000)))
    add(nums=list(range(99999, -1, -1)))
    for n in range(2, 6):
        for p in permutations(range(n)):
            add(nums=list(p))
    while len(calls) < 600:
        n = rng.randint(2, 60)
        nums = list(range(n))
        rng.shuffle(nums)
        assert sorted(nums) == list(range(n)) and 2 <= n <= 100000
        add(nums=nums)
    assert len(calls) == 600
    return list(calls)
