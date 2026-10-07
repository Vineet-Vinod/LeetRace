import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(words):
        assert 1 <= len(words) <= 20000
        assert all(
            1 <= len(w) <= 26
            and len(set(w)) == len(w)
            and all("a" <= c <= "z" for c in w)
            for w in words
        )
        call = (
            "candidate("
            + ", ".join(f"{name}={value!r}" for name, value in (("words", words),))
            + ")"
        )
        calls[call] = None

    add(words=["a", "b", "ab", "cde"])
    add(words=["a", "ab", "abc"])
    add(words=["abcdefghijklmnopqrstuvwxyz"] * 20000)
    add(words=["a"])
    while len(calls) < 600:
        n = rng.randint(1, 35)
        mode = rng.randrange(4)
        if mode == 0:
            base = rng.sample("abcdefghijklmnopqrstuvwxyz", rng.randint(1, 24))
            words = ["".join(base[: rng.randint(1, len(base))]) for _ in range(n)]
        elif mode == 1:
            words = [
                "".join(rng.sample("abcdefghijklmnopqrstuvwxyz", rng.randint(1, 26)))
                for _ in range(n)
            ]
        elif mode == 2:
            words = ["".join(rng.sample("abcde", rng.randint(1, 5))) for _ in range(n)]
        else:
            words = [
                rng.choice(["abc", "defghi", "jklmnopqr", "stuvwxyz"]) for _ in range(n)
            ]
        add(words=words)
    return list(calls)
