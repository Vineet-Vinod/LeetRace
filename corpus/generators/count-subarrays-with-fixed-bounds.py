import random


def sample(r, turn):
    n = r.randint(2, 65)
    low = r.randint(1, 20)
    high = r.randint(1, 20)
    if turn % 4 != 0:
        low, high = min(low, high), max(low, high)
    a = [r.choice([low, high, r.randint(1, 25)]) for _ in range(n)]
    return dict(nums=a, minK=low, maxK=high)


def validate(nums, minK, maxK):
    assert 2 <= len(nums) <= 100000 and all(
        1 <= v <= 10**6 for v in nums + [minK, maxK]
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

    add(nums=[1, 3, 5, 2, 7, 5], minK=1, maxK=5)
    add(nums=[1, 1, 1, 1], minK=1, maxK=1)
    add(nums=[10**6] * 100000, minK=10**6, maxK=10**6)
    turn = 0
    while len(calls) < 600:
        kwargs = sample(r, turn)
        turn += 1
        add(**kwargs)
    assert len(calls) == len(set(calls)) == 600
    return calls
