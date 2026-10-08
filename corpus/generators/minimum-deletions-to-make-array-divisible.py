import random


def sample(r, turn):
    a = [r.randint(1, 40) for _ in range(r.randint(1, 50))]
    d = [r.randint(1, 40) for _ in range(r.randint(1, 50))]
    if turn % 3 == 0:
        base = r.choice(a)
        d = [base * r.randint(1, 25) for _ in d]
    if turn % 3 == 1:
        a = [r.randint(2, 40) for _ in a]
        d = [1] + d
    return dict(nums=a, numsDivide=d)


def validate(nums, numsDivide):
    assert (
        1 <= len(nums) <= 100000
        and 1 <= len(numsDivide) <= 100000
        and all(1 <= v <= 10**9 for v in nums + numsDivide)
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

    add(nums=[2, 3, 2, 4, 3], numsDivide=[9, 6, 9, 3, 15])
    add(nums=[4, 3, 6], numsDivide=[8, 2, 6, 10])
    add(nums=[10**9] * 100000, numsDivide=[10**9] * 100000)
    turn = 0
    while len(calls) < 600:
        kwargs = sample(r, turn)
        turn += 1
        add(**kwargs)
    assert len(calls) == len(set(calls)) == 600
    return calls
