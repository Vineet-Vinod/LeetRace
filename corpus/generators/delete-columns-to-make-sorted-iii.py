import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        rows = kwargs["strs"]
        assert 1 <= len(rows) <= 100 and 1 <= len(rows[0]) <= 100
        assert all(
            len(s) == len(rows[0]) and s.isascii() and s.islower() and s.isalpha()
            for s in rows
        )
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(strs=["z" * 100] * 100)
    add(strs=[("zyxwvutsrqponmlkjihgfedcba" * 4)[:100]] * 100)
    add(strs=["babca", "bbazb"])
    add(strs=["edcba"])
    add(strs=["ghi", "def", "abc"])
    while len(calls) < 600:
        n = rng.randint(1, 8)
        m = rng.randint(1, 20)
        strs = ["".join(rng.choices("abcxyz", k=m)) for _ in range(n)]
        if len(calls) % 4 == 0:
            strs = ["".join(sorted(s)) for s in strs]
        add(strs=strs)
    return calls
