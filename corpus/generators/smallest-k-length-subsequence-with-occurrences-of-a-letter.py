import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        s, k, c, r = kw["s"], kw["k"], kw["letter"], kw["repetition"]
        assert (
            1 <= r <= k <= len(s) <= 50000
            and s.isascii()
            and s.isalpha()
            and s.islower()
        )
        assert len(c) == 1 and "a" <= c <= "z" and s.count(c) >= r
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kw.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for kw in [
        {"s": "leet", "k": 3, "letter": "e", "repetition": 1},
        {"s": "leetcode", "k": 4, "letter": "e", "repetition": 2},
        {"s": "bb", "k": 2, "letter": "b", "repetition": 2},
    ] + [
        {"s": "za" * 25000, "k": 25000, "letter": "z", "repetition": 12500},
        {"s": "z" * 49999 + "a", "k": 1, "letter": "a", "repetition": 1},
        {"s": "a" * 50000, "k": 50000, "letter": "a", "repetition": 50000},
    ]:
        add(**kw)
    while len(calls) < 600:
        n = rng.randint(1, 70)
        s = "".join(rng.choice("abcdez") for _ in range(n))
        c = rng.choice(s)
        r = rng.randint(1, s.count(c))
        k = rng.randint(r, n)
        add(s=s, k=k, letter=c, repetition=r)
    return calls
