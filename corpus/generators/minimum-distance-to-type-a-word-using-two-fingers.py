import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        s = kwargs["word"]
        assert 2 <= len(s) <= 300 and set(s) <= set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(word="CAKE")
    add(word="HAPPY")
    add(word="A" * 300)
    add(word=("ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 12)[:300])
    add(word="AZ")
    while len(calls) < 600:
        n = rng.randint(2, 60)
        s = "".join(rng.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=n))
        if len(calls) % 4 == 0:
            s = "".join(rng.choices("AZ", k=n))
        add(word=s)
    return calls
