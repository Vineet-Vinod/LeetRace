import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def emit(**values):
        s = values["s"]
        assert 1 <= len(s) <= 500 and s.isascii() and s.isalpha() and s.islower()
        call = (
            "candidate("
            + ", ".join(name + "=" + repr(value) for name, value in values.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for s in [
        "a",
        "zzazz",
        "mbadm",
        "leetcode",
        "a" * 500,
        "abcdefghijklmnopqrstuvwxyz" * 19 + "abcdef",
        "ab" * 250,
    ]:
        emit(s=s)
    while len(calls) < 600:
        s = "".join(rng.choices("abcde", k=rng.randint(1, 60)))
        if len(calls) % 4 == 0:
            s = s + s[::-1]
        emit(s=s)
    return calls
