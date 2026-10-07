import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        nums, q = kw["nums"], kw["quantity"]
        assert (
            1 <= len(nums) <= 100000
            and len(set(nums)) <= 50
            and all(1 <= v <= 1000 for v in nums)
        )
        assert 1 <= len(q) <= 10 and all(1 <= v <= 100000 for v in q)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kw.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for kw in [
        {"nums": [1, 2, 3, 4], "quantity": [2]},
        {"nums": [1, 2, 3, 3], "quantity": [2]},
        {"nums": [1, 1, 2, 2], "quantity": [2, 2]},
    ] + [
        {"nums": [1000] * 100000, "quantity": [100000]},
        {"nums": [i % 50 + 1 for i in range(100000)], "quantity": [2000] * 10},
        {"nums": [1], "quantity": [100000] * 10},
    ]:
        add(**kw)
    while len(calls) < 600:
        m = rng.randint(1, 7)
        q = [rng.randint(1, 12) for _ in range(m)]
        if len(calls) % 3 == 0:
            nums = []
            for i, v in enumerate(q):
                nums.extend([i + 1] * (v + rng.randint(0, 3)))
        elif len(calls) % 3 == 1:
            nums = [rng.randint(1, 8) for _ in range(rng.randint(1, 50))]
            q[rng.randrange(m)] = len(nums) + 1
        else:
            nums = [rng.randint(1, 8) for _ in range(rng.randint(1, 70))]
        rng.shuffle(nums)
        add(nums=nums, quantity=q)
    return calls
