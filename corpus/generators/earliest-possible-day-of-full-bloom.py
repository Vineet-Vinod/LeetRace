import random

EXAMPLES = [
    "candidate(plantTime=[1, 4, 3], growTime=[2, 3, 1])",
    "candidate(plantTime=[1, 2, 3, 2], growTime=[2, 1, 2, 1])",
    "candidate(plantTime=[1], growTime=[1])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = list(EXAMPLES)
    seen = set(calls)

    def emit(call: str) -> None:
        if call not in seen:
            calls.append(call)
            seen.add(call)

    def add(plant, grow):
        assert 1 <= len(plant) == len(grow) <= 100000
        assert all(1 <= v <= 10000 for v in plant + grow)
        emit(f"candidate(plantTime={plant!r}, growTime={grow!r})")

    add([10000] * 100000, [10000] * 100000)
    add([1], [10000])
    add([10000], [1])
    while len(calls) < 600:
        n = rng.randint(1, 40)
        plant = [rng.randint(1, 10000) for _ in range(n)]
        grow = [rng.randint(1, 10000) for _ in range(n)]
        if rng.random() < 0.25:
            grow = [rng.randint(1, 10000)] * n
        add(plant, grow)
    return calls
