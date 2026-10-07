import random


def sample(r, turn):
    n = r.randint(1, 60)
    k = r.randint(1, n)
    a = [r.randrange(2) for _ in range(n)]
    if turn % 3 == 0:
        a = [1] * n
        for _ in range(r.randint(1, 15)):
            start = r.randrange(n - k + 1)
            for i in range(start, start + k):
                a[i] ^= 1
    return dict(nums=a, k=k)


def validate(nums, k):
    assert 1 <= k <= len(nums) <= 100000 and all(v in (0, 1) for v in nums)


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

    add(nums=[0, 1, 0], k=1)
    add(nums=[1, 1, 0], k=2)
    add(nums=[0, 0, 0, 1, 0, 1, 1, 0], k=3)
    add(nums=[0] * 100000, k=1)
    add(nums=[0] * 100000, k=100000)
    turn = 0
    while len(calls) < 600:
        kwargs = sample(r, turn)
        turn += 1
        add(**kwargs)
    assert len(calls) == len(set(calls)) == 600
    return calls
