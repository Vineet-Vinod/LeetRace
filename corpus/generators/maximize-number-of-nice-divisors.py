import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def emit(**values):
        assert 1 <= values["primeFactors"] <= 1000000000
        call = (
            "candidate("
            + ", ".join(name + "=" + repr(value) for name, value in values.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for n in list(range(1, 100)) + [999999998, 999999999, 1000000000]:
        emit(primeFactors=n)
    while len(calls) < 600:
        emit(primeFactors=rng.randint(1, 1000000000))
    return calls
