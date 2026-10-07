import random


def sample(r, turn):
    n = r.randint(1, 65)
    a = sorted(r.randint(1, r.randint(1, 20)) for _ in range(n))
    k = r.randint(1, n)
    if turn % 3 == 0:
        k = 1
    if turn % 3 == 1:
        k = max(1, n // max(a.count(v) for v in set(a)))
    return dict(nums=a, k=k)


def validate(nums, k):
    assert (
        1 <= k <= len(nums) <= 100000
        and nums == sorted(nums)
        and all(1 <= v <= 100000 for v in nums)
    )


def generate(seed: int = 0) -> list[str]:
    r = random.Random(seed)
    calls = []
    seen = set()

    def add(**kwargs):
        validate(**kwargs)
        parts = []
        for key, value in kwargs.items():
            expression = repr(value)
            parts.append(key + "=" + expression)
        call = "candidate(" + ", ".join(parts) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(nums=[1, 2, 2, 3, 3, 4, 4], k=3)
    add(nums=[5, 6, 6, 7, 8], k=3)
    add(nums=list(range(1, 100001)), k=100000)
    add(nums=[100000] * 100000, k=2)
    turn = 0
    while len(calls) < 600:
        kwargs = sample(r, turn)
        turn += 1
        add(**kwargs)
    assert len(calls) == len(set(calls)) == 600
    return calls
