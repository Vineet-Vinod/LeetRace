import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(tires: list[list[int]], changeTime: int, numLaps: int) -> None:
        assert 1 <= len(tires) <= 100000 and all(
            len(t) == 2 and 1 <= t[0] <= 100000 and 2 <= t[1] <= 100000 for t in tires
        )
        assert 1 <= changeTime <= 100000 and 1 <= numLaps <= 1000
        call = (
            "candidate("
            + ", ".join(
                f"{key}={value!r}"
                for key, value in [
                    ("tires", tires),
                    ("changeTime", changeTime),
                    ("numLaps", numLaps),
                ]
            )
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(tires=[[2, 3], [3, 4]], changeTime=5, numLaps=4)
    add(tires=[[1, 2]] * 100000, changeTime=100000, numLaps=1000)
    add(tires=[[100000, 100000]], changeTime=1, numLaps=1000)
    add(tires=[[2, 3], [3, 4]], changeTime=5, numLaps=4)
    add(tires=[[1, 10], [2, 2], [3, 4]], changeTime=6, numLaps=5)
    while len(calls) < 600:
        tires = [
            [rng.randint(1, 100), rng.randint(2, 15)] for _ in range(rng.randint(1, 15))
        ]
        add(
            tires=tires,
            changeTime=rng.choice([1, 100000, rng.randint(1, 200)]),
            numLaps=rng.randint(1, 50),
        )
    return calls
