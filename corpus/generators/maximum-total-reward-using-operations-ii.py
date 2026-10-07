import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(rewardValues: list[int]) -> None:
        assert 1 <= len(rewardValues) <= 50000 and all(
            1 <= x <= 50000 for x in rewardValues
        )
        call = (
            "candidate("
            + ", ".join(
                f"{key}={value!r}" for key, value in [("rewardValues", rewardValues)]
            )
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(rewardValues=[1, 1, 3, 3])
    add(rewardValues=list(range(1, 50001)))
    add(rewardValues=[50000] * 50000)
    add(rewardValues=[1, 1, 3, 3])
    add(rewardValues=[1, 6, 4, 3, 2])
    while len(calls) < 600:
        n = rng.randint(1, 40)
        values = [rng.randint(1, 150) for _ in range(n)]
        if len(calls) % 4 == 0:
            values = [rng.randint(1, 50000)] * n
        add(rewardValues=values)
    return calls
