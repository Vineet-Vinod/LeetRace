import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(houses: list[int], k: int) -> None:
        assert 1 <= k <= len(houses) <= 100
        assert len(set(houses)) == len(houses) and all(1 <= x <= 10000 for x in houses)
        call = (
            "candidate("
            + ", ".join(
                f"{key}={value!r}" for key, value in [("houses", houses), ("k", k)]
            )
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(houses=[1, 4, 8, 10, 20], k=3)
    add(houses=list(range(1, 101)), k=1)
    add(houses=list(range(9901, 10001)), k=100)
    add(houses=[1, 4, 8, 10, 20], k=3)
    add(houses=[2, 3, 5, 12, 18], k=2)
    while len(calls) < 600:
        n = rng.randint(1, 35)
        houses = rng.sample(range(1, 10001), n)
        add(houses=houses, k=rng.choice([1, n, rng.randint(1, n)]))
    return calls
