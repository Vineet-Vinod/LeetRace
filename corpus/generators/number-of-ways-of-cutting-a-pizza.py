import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def valid(d):
        g = d["pizza"]
        assert (
            1 <= len(g) <= 50
            and 1 <= len(g[0]) <= 50
            and all(len(row) == len(g[0]) and set(row) <= set("A.") for row in g)
            and 1 <= d["k"] <= 10
        )

    def add(**kwargs):
        valid(kwargs)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(pizza=["A..", "AAA", "..."], k=3)
    add(pizza=["A..", "AA.", "..."], k=3)
    add(pizza=["A..", "A..", "..."], k=1)
    add(pizza=["A" * 50] * 50, k=10)
    add(pizza=["." * 50] * 50, k=10)
    add(pizza=["A" + "." * 49] + ["." * 50] * 49, k=1)
    t = 0
    while len(calls) < 600:
        r, c = rng.randint(1, 9), rng.randint(1, 9)
        p = rng.choice([0.1, 0.4, 0.8, 1])
        pizza = [
            "".join("A" if rng.random() < p else "." for _ in range(c))
            for _ in range(r)
        ]
        add(pizza=pizza, k=rng.randint(1, 10))
        t += 1
    return calls
