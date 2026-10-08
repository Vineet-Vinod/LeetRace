import random


def sample(r, turn):
    n = r.randint(1, 65)
    a = [r.randint(1, r.choice([1, 3, 10, 100000])) for _ in range(n)]
    if turn % 4 == 0:
        a = list(range(1, n + 1))
    return dict(nums=a)


def validate(nums):
    assert 1 <= len(nums) <= 100000 and all(1 <= v <= 100000 for v in nums)


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

    add(nums=[1, 2, 3])
    add(nums=[3, 4, 3, 4, 5])
    add(nums=[4, 3, 5, 4])
    add(nums=list(range(1, 100001)))
    add(nums=[100000] * 100000)
    turn = 0
    while len(calls) < 600:
        kwargs = sample(r, turn)
        turn += 1
        add(**kwargs)
    assert len(calls) == len(set(calls)) == 600
    return calls
