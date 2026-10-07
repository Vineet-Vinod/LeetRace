import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def emit(**values):
        assert 1 <= values["n"] <= 1000
        call = (
            "candidate("
            + ", ".join(name + "=" + repr(value) for name, value in values.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    # Smallest varied sizes keep the unavoidable quadratic output suite practical.
    sizes = list(range(1, 500)) + [1000]
    rng.shuffle(sizes)
    for n in sizes:
        emit(n=n)
    return calls
