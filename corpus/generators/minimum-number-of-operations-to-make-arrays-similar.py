import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        a, b = kwargs["nums"], kwargs["target"]
        assert 1 <= len(a) == len(b) <= 100000
        assert all(1 <= x <= 10**6 for x in a + b)
        # Equal sums and equal parity counts are exactly the reachability invariants.
        assert sum(a) == sum(b) and sum(x % 2 for x in a) == sum(x % 2 for x in b)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(nums=[8, 12, 6], target=[2, 14, 10])
    add(nums=[1, 2, 5], target=[4, 1, 3])
    add(nums=[1, 1, 1, 1, 1], target=[1, 1, 1, 1, 1])
    add(nums=[1] * 100000, target=[1] * 100000)
    add(nums=[2, 1000000], target=[500000, 500002])
    add(nums=[1000000], target=[1000000])
    while len(calls) < 600:
        n = rng.randint(1, 40)
        a = [rng.randint(1, 1000) for _ in range(n)]
        b = a.copy()
        if n > 1:
            for _ in range(rng.randint(0, 30)):
                i, j = rng.sample(range(n), 2)
                if b[j] > 2 and b[i] <= 999998:
                    b[i] += 2
                    b[j] -= 2
        rng.shuffle(b)
        add(nums=a, target=b)
    return calls
