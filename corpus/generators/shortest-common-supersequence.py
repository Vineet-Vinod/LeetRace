import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        calls[
            "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        ] = None

    add(str1="a" * 1000, str2="z" * 1000)
    add(str1="ab" * 500, str2="ba" * 500)
    add(str1="abac", str2="cab")
    while len(calls) < 600:
        a = "".join(rng.choice("abcde") for _ in range(rng.randint(1, 35)))
        b = "".join(rng.choice("abcde") for _ in range(rng.randint(1, 35)))
        if len(calls) % 4 == 0:
            b = a
        assert (
            1 <= len(a) <= 1000 and 1 <= len(b) <= 1000 and a.islower() and b.islower()
        )
        add(str1=a, str2=b)
    assert len(calls) == 600
    return list(calls)
