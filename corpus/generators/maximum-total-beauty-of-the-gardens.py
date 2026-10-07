import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def emit(**values):
        flowers = values["flowers"]
        assert 1 <= len(flowers) <= 100000 and all(1 <= x <= 100000 for x in flowers)
        assert (
            1 <= values["target"] <= 100000
            and 1 <= values["newFlowers"] <= 10000000000
            and 1 <= values["full"] <= 100000
            and 1 <= values["partial"] <= 100000
        )
        call = (
            "candidate("
            + ", ".join(name + "=" + repr(value) for name, value in values.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    emit(flowers=[1, 3, 1, 1], newFlowers=7, target=6, full=12, partial=1)
    emit(flowers=[2, 4, 5, 3], newFlowers=10, target=5, full=2, partial=6)
    emit(
        flowers=[1] * 100000,
        newFlowers=10000000000,
        target=100000,
        full=100000,
        partial=100000,
    )
    emit(flowers=[100000] * 100000, newFlowers=1, target=1, full=1, partial=1)
    emit(
        flowers=list(range(1, 100001)),
        newFlowers=100000,
        target=100000,
        full=10,
        partial=5,
    )
    while len(calls) < 600:
        n = rng.randint(1, 25)
        target = rng.randint(1, 30)
        emit(
            flowers=[rng.randint(1, 40) for _ in range(n)],
            newFlowers=rng.randint(1, 300),
            target=target,
            full=rng.randint(1, 40),
            partial=rng.randint(1, 40),
        )
    return calls
