import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        calls[
            "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        ] = None

    add(s="a" * 150)
    add(s="abcdefghijklmnopqrstuvwxyz" * 5 + "abcdefghijklmnopqrst")
    for s in ("aaa", "aaaaa", "aaaaaaaaaa", "abbbabbbcabbbabbbc", "aabcaabcd"):
        add(s=s)
    while len(calls) < 600:
        unit = "".join(rng.choice("abcde") for _ in range(rng.randint(1, 6)))
        s = unit * rng.randint(1, 8)
        if len(calls) % 3 == 0:
            s += "".join(rng.choice("abc") for _ in range(rng.randint(1, 5)))
        assert 1 <= len(s) <= 150 and s.isalpha() and s.islower()
        add(s=s)
    assert len(calls) == 600
    return list(calls)
