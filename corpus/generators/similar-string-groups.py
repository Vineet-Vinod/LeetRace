import random
from collections import Counter


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        validate(kwargs)
        call = (
            "candidate(" + ", ".join(k + "=" + repr(v) for k, v in kwargs.items()) + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    def letters(text):
        return all("a" <= ch <= "z" for ch in text)

    def array(values, minimum, maximum, length):
        assert 1 <= len(values) <= length
        assert all(minimum <= v <= maximum for v in values)

    def validate(d):
        strs = d["strs"]
        assert 1 <= len(strs) <= 300
        assert all(
            1 <= len(w) <= 300 and letters(w) and Counter(w) == Counter(strs[0])
            for w in strs
        )

    add(strs=["tars", "rats", "arts", "star"])
    add(strs=["omv", "ovm"])
    add(strs=["a" * 300] * 300)
    while len(calls) < 600:
        base = list("".join(rng.choice("abcde") for _ in range(rng.randint(1, 15))))
        strs = []
        for _ in range(rng.randint(1, 30)):
            rng.shuffle(base)
            strs.append("".join(base))
        add(strs=strs)
    assert len(calls) == 600
    return calls
