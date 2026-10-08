import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(words):
        assert 1 <= len(words) <= 100000
        assert sum(map(len, words)) <= 500000
        assert all(
            1 <= len(w) <= 100000 and all("a" <= c <= "z" for c in w) for w in words
        )
        call = (
            "candidate("
            + ", ".join(f"{name}={value!r}" for name, value in (("words", words),))
            + ")"
        )
        calls[call] = None

    add(words=["a", "aba", "ababa", "aa"])
    add(words=["pa", "papa", "ma", "mama"])
    add(words=["abab", "ab"])
    add(words=["abcde"] * 100000)
    add(words=["a" * 100000] * 5)
    add(words=["z"])
    while len(calls) < 600:
        mode = rng.randrange(4)
        n = rng.randint(1, 25)
        if mode == 0:
            base = "".join(rng.choices("abc", k=rng.randint(1, 6)))
            words = [base * rng.randint(1, 8) for _ in range(n)]
        elif mode == 1:
            base = "".join(rng.choices("abcd", k=rng.randint(1, 5)))
            words = [base, base + "x" + base] * rng.randint(1, 12)
        elif mode == 2:
            words = [
                "".join(rng.choices("abcdef", k=rng.randint(1, 15))) for _ in range(n)
            ]
        else:
            words = ["a" * rng.randint(1, 15) for _ in range(n)]
        add(words=words)
    return list(calls)
