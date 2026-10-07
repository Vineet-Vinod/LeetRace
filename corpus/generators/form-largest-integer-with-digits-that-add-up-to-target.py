import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def emit(**values):
        cost, target = values["cost"], values["target"]
        assert (
            len(cost) == 9 and 1 <= target <= 5000 and all(1 <= c <= 5000 for c in cost)
        )
        call = (
            "candidate("
            + ", ".join(name + "=" + repr(value) for name, value in values.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for cost, target in [
        ([1] * 9, 5000),
        ([5000] * 9, 5000),
        ([5000] * 9, 4999),
        ([4, 3, 2, 5, 6, 7, 2, 5, 5], 9),
        ([2] * 9, 5),
        ([7, 6, 5, 5, 5, 6, 8, 7, 8], 12),
    ]:
        emit(cost=cost, target=target)
    while len(calls) < 600:
        cost = [rng.randint(1, 50) for _ in range(9)]
        target = rng.randint(1, 150)
        if len(calls) % 3 == 0:
            cost = [2 * c for c in cost]
            target = 2 * target + 1
        elif len(calls) % 3 == 1:
            target = sum(rng.choices(cost, k=rng.randint(1, 5)))
        emit(cost=cost, target=target)
    return calls
