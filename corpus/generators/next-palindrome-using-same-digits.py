import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        calls[
            "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        ] = None

    add(num="9" * 100000)
    add(num="1" + "0" * 49998 + "2" + "2" + "0" * 49998 + "1")
    for x in "0123456789":
        add(num=x)
    while len(calls) < 600:
        half = "".join(rng.choice("0123456789") for _ in range(rng.randint(1, 35)))
        if len(calls) % 3 == 0:
            half = "".join(sorted(half, reverse=True))
        mid = rng.choice("0123456789") if rng.randrange(2) else ""
        num = half + mid + half[::-1]
        assert 1 <= len(num) <= 100000 and num == num[::-1] and num.isdigit()
        add(num=num)
    assert len(calls) == 600
    return list(calls)
