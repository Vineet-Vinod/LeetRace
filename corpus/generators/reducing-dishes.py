import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def emit(**values):
        satisfaction = values["satisfaction"]
        assert 1 <= len(satisfaction) <= 500 and all(
            -1000 <= x <= 1000 for x in satisfaction
        )
        call = (
            "candidate("
            + ", ".join(name + "=" + repr(value) for name, value in values.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for satisfaction in [
        [-1, -8, 0, 5, -9],
        [4, 3, 2],
        [-1, -4, -5],
        [-1000] * 500,
        [1000] * 500,
        [0] * 500,
    ]:
        emit(satisfaction=satisfaction)
    while len(calls) < 600:
        n = rng.randint(1, 100)
        mode = len(calls) % 4
        low, high = (
            (-1000, -1) if mode == 0 else (0, 1000) if mode == 1 else (-1000, 1000)
        )
        emit(satisfaction=[rng.randint(low, high) for _ in range(n)])
    return calls
