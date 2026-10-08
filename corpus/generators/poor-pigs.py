import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**data) -> None:
        b, d, t = data["buckets"], data["minutesToDie"], data["minutesToTest"]
        assert 1 <= b <= 1000 and 1 <= d <= t <= 100
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in data.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for example in [
        {"buckets": 4, "minutesToDie": 15, "minutesToTest": 15},
        {"buckets": 4, "minutesToDie": 15, "minutesToTest": 30},
    ]:
        add(**example)
    add(buckets=1, minutesToDie=100, minutesToTest=100)
    add(buckets=1000, minutesToDie=1, minutesToTest=100)
    add(buckets=1000, minutesToDie=100, minutesToTest=100)
    for base in range(2, 11):
        for exponent in range(1, 10):
            for b in [base**exponent - 1, base**exponent, base**exponent + 1]:
                if 1 <= b <= 1000:
                    add(buckets=b, minutesToDie=1, minutesToTest=base - 1)
    while len(calls) < 600:
        d = rng.randint(1, 100)
        add(
            buckets=rng.randint(1, 1000),
            minutesToDie=d,
            minutesToTest=rng.randint(d, 100),
        )
    assert len(calls) == 600
    return calls
