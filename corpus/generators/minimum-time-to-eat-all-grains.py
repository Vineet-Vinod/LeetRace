import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def emit(**values):
        hens, grains = values["hens"], values["grains"]
        assert (
            1 <= len(hens) <= 20000
            and 1 <= len(grains) <= 20000
            and all(0 <= x <= 1000000000 for x in hens + grains)
        )
        call = (
            "candidate("
            + ", ".join(name + "=" + repr(value) for name, value in values.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for hens, grains in [
        ([0], [0]),
        ([0], [1000000000]),
        ([1000000000], [0]),
        ([3, 6, 7], [2, 4, 7, 9]),
        ([4, 6, 109, 111, 213, 215], [5, 110, 214]),
        ([0] * 20000, [1000000000] * 20000),
        (list(range(20000)), list(range(20000))),
    ]:
        emit(hens=hens, grains=grains)
    while len(calls) < 600:
        hens = [rng.randint(0, 100) for _ in range(rng.randint(1, 20))]
        grains = [rng.randint(0, 100) for _ in range(rng.randint(1, 20))]
        if len(calls) % 4 == 0:
            grains = rng.choices(hens, k=rng.randint(1, 20))
        emit(hens=hens, grains=grains)
    return calls
