import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        assert (
            2 <= kwargs["n"] <= 28
            and 1 <= kwargs["firstPlayer"] < kwargs["secondPlayer"] <= kwargs["n"]
        )
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(n=28, firstPlayer=1, secondPlayer=28)
    add(n=28, firstPlayer=2, secondPlayer=4)
    add(n=2, firstPlayer=1, secondPlayer=2)
    add(n=11, firstPlayer=2, secondPlayer=4)
    add(n=5, firstPlayer=1, secondPlayer=5)
    while len(calls) < 600:
        n = rng.randint(2, 28)
        a, b = sorted(rng.sample(range(1, n + 1), 2))
        add(n=n, firstPlayer=a, secondPlayer=b)
    return calls
