import random


def sample(r, turn):
    n = r.randint(1, 40)
    k = r.choice(list(range(1, n + 1, 2)))
    a = [r.randint(-30, 30) for _ in range(n)]
    if turn % 4 == 0:
        a = [-r.randint(1, 30) for _ in range(n)]
    if turn % 4 == 1:
        a = [r.randint(0, 30) for _ in range(n)]
    return dict(nums=a, k=k)


def validate(nums, k):
    assert 1 <= len(nums) <= 10000 and all(-(10**9) <= v <= 10**9 for v in nums)
    assert 1 <= k <= len(nums) and k % 2 == 1 and len(nums) * k <= 10**6


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

    add(nums=[1, 2, 3, -1, 2], k=3)
    add(nums=[12, -2, -2, -2, -2], k=5)
    add(nums=[-1, -2, -3], k=1)
    add(nums=[-(10**9), 10**9] * 5000, k=99)
    add(nums=[-(10**9), 10**9] * 4000, k=125)
    add(nums=[-(10**9)] * 999, k=999)
    turn = 0
    while len(calls) < 600:
        kwargs = sample(r, turn)
        turn += 1
        add(**kwargs)
    assert len(calls) == len(set(calls)) == 600
    return calls
