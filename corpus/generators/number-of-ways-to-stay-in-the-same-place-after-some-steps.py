import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        s, n = kwargs["steps"], kwargs["arrLen"]
        assert 1 <= s <= 500 and 1 <= n <= 1000000
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(steps=3, arrLen=2)
    add(steps=2, arrLen=4)
    add(steps=4, arrLen=2)
    add(steps=500, arrLen=1000000)
    add(steps=500, arrLen=1)
    add(steps=1, arrLen=1)
    while len(calls) < 600:
        add(
            steps=rng.randint(1, 70),
            arrLen=rng.choice([rng.randint(1, 50), rng.randint(1, 1000000)]),
        )
    return calls
