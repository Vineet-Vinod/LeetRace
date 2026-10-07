import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**data) -> None:
        n = data["n"]
        assert 1 <= n <= 800000000
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in data.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for example in [{"n": 9}, {"n": 10}]:
        add(**example)
    add(n=1)
    add(n=800000000)
    for exponent in range(1, 10):
        for n in [9**exponent - 1, 9**exponent, 9**exponent + 1]:
            if n <= 800000000:
                add(n=n)
    for n in range(1, 101):
        add(n=n)
    while len(calls) < 600:
        add(n=rng.randint(1, 800000000))
    assert len(calls) == 600
    return calls
