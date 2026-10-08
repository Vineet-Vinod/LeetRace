import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        assert (
            1 <= len(kw["s"]) <= 4000
            and kw["s"].isascii()
            and kw["s"].isalpha()
            and kw["s"].islower()
        )
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kw.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for kw in [{"s": "abcabcdabc"}, {"s": "aaabaab"}, {"s": "aaaaa"}] + [
        {"s": "a" * 4000},
        {"s": "ab" * 2000},
        {"s": "z"},
    ]:
        add(**kw)
    while len(calls) < 600:
        n = rng.randint(1, 65)
        mode = len(calls) % 3
        if mode == 0:
            block = "".join(rng.choice("abc") for _ in range(rng.randint(1, 6)))
            s = (block * n)[:n]
        else:
            s = "".join(
                rng.choice("ab" if mode == 1 else "abcdefghijklmnopqrstuvwxyz")
                for _ in range(n)
            )
        add(s=s)
    return calls
