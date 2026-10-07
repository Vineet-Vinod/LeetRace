import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        calls[
            "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        ] = None

    add(s="a" * 200000, k=200000)
    add(s="abcdefghijklmnopqrstuvwxyz" * 7692 + "abcdefgh", k=26)
    while len(calls) < 600:
        alphabet = "abcdefghijklmnopqrstuvwxyz"[: rng.randint(1, 26)]
        counts = [rng.randint(1, 12) for _ in alphabet]
        s = "".join(c * x for c, x in zip(alphabet, counts))
        chars = list(s)
        rng.shuffle(chars)
        s = "".join(chars)
        k = rng.randint(1, len(alphabet)) if len(calls) % 3 else rng.randint(1, len(s))
        assert 1 <= len(s) <= 200000 and 1 <= k <= len(s) and s.islower()
        add(s=s, k=k)
    assert len(calls) == 600
    return list(calls)
