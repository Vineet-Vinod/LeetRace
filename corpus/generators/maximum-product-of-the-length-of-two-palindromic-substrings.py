import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def emit(**values):
        s = values["s"]
        assert 2 <= len(s) <= 100000 and s.isascii() and s.isalpha() and s.islower()
        call = (
            "candidate("
            + ", ".join(name + "=" + repr(value) for name, value in values.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for s in [
        "aa",
        "ab",
        "ababbb",
        "zaaaxbbby",
        "a" * 100000,
        "ab" * 50000,
        "abcdefghijklmnopqrstuvwxyz" * 3846 + "abcd",
    ]:
        emit(s=s)
    while len(calls) < 600:
        n = rng.randint(2, 100)
        s = "".join(rng.choices("abcde", k=n))
        if len(calls) % 3 == 0:
            part = "".join(rng.choices("abc", k=rng.randint(1, 15)))
            s = part + "x" + part[::-1] + "y" + part + "z" + part[::-1]
        emit(s=s)
    return calls
