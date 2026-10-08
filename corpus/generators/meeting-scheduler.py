import random


def make_slots(rng):
    intervals = []
    start = rng.randint(0, 10)
    for _ in range(rng.randint(1, 10)):
        start += rng.randint(1, 20)
        end = start + rng.randint(1, 20)
        intervals.append([start, end])
        start = end + rng.randint(0, 20)
    return intervals


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        first = make_slots(rng)
        second = make_slots(rng)
        duration = rng.randint(1, 20)
        key = (tuple(map(tuple, first)), tuple(map(tuple, second)), duration)
        if key not in seen:
            seen.add(key)
            assert all(a < b for a, b in first + second)
            cases.append(
                f"candidate(slots1={first!r}, slots2={second!r}, duration={duration})"
            )
    return cases
