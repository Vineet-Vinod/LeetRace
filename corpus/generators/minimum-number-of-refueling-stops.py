import random

EXAMPLES = [
    "candidate(target=1, startFuel=1, stations=[])",
    "candidate(target=100, startFuel=1, stations=[[10, 100]])",
    "candidate(target=100, startFuel=10, stations=[[10, 60], [20, 30], [30, 30], [60, 40]])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = list(EXAMPLES)
    seen = set(calls)

    def emit(call: str) -> None:
        if call not in seen:
            calls.append(call)
            seen.add(call)

    def add(target, fuel, stations):
        assert 1 <= target <= 10**9 and 1 <= fuel <= 10**9 and 0 <= len(stations) <= 500
        assert all(
            len(p) == 2 and 1 <= p[0] < target and 1 <= p[1] < 10**9 for p in stations
        )
        assert all(a[0] < b[0] for a, b in zip(stations, stations[1:]))
        emit(f"candidate(target={target}, startFuel={fuel}, stations={stations!r})")

    add(10**9, 10**9, [[i, 10**9 - 1] for i in range(1, 501)])
    add(10**9, 1, [])
    add(1, 1, [])
    while len(calls) < 600:
        target = rng.randint(2, 1000)
        n = rng.randint(0, min(35, target - 1))
        positions = sorted(rng.sample(range(1, target), n))
        stations = [[p, rng.randint(1, 250)] for p in positions]
        mode = rng.randrange(4)
        fuel = rng.randint(1, target)
        if mode == 0:
            fuel = target + rng.randint(0, 100)
        if mode == 1 and stations:
            fuel = stations[0][0]
            for i, row in enumerate(stations):
                row[1] = (stations[i + 1][0] if i + 1 < n else target) - row[0]
        add(target, fuel, stations)
    return calls
