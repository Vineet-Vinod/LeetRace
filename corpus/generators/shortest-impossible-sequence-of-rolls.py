import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def emit(**values):
        rolls, k = values["rolls"], values["k"]
        assert (
            1 <= len(rolls) <= 100000
            and 1 <= k <= 100000
            and all(1 <= x <= k for x in rolls)
        )
        call = (
            "candidate("
            + ", ".join(name + "=" + repr(value) for name, value in values.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for rolls, k in [
        ([1], 1),
        ([1] * 100000, 1),
        (list(range(1, 100001)), 100000),
        ([100000] * 100000, 100000),
        ([4, 2, 1, 2, 3, 3, 2, 4, 1], 4),
        ([1, 1, 2, 2], 2),
    ]:
        emit(rolls=rolls, k=k)
    while len(calls) < 600:
        k = rng.randint(1, 20)
        if len(calls) % 3 == 0:
            rolls = []
            for _ in range(rng.randint(1, 20)):
                block = list(range(1, k + 1))
                rng.shuffle(block)
                rolls.extend(block)
        else:
            rolls = [rng.randint(1, k) for _ in range(rng.randint(1, 100))]
        emit(rolls=rolls, k=k)
    return calls
