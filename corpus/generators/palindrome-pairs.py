import random
from itertools import product


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
        words = d["words"]
        assert 1 <= len(words) <= 5000 and len(set(words)) == len(words)
        assert all(0 <= len(w) <= 300 and letters(w) for w in words)

    add(words=["abcd", "dcba", "lls", "s", "sssll"])
    add(words=["a", ""])
    add(words=["a" * 300, "a" * 299, ""])
    add(
        words=["".join(p) for p in product("abcdefghijklmnopqrstuvwxyz", repeat=3)][
            :5000
        ]
    )
    add(
        words=[
            "".join(p) + "a" * 297 for p in product("abcdefghijklmnopqrst", repeat=3)
        ][:5000]
    )
    while len(calls) < 600:
        words = set()
        for _ in range(rng.randint(2, 30)):
            w = "".join(rng.choice("abcde") for _ in range(rng.randint(0, 12)))
            words.add(w)
            if rng.randrange(2):
                words.add(w[::-1])
        if rng.randrange(4) == 0:
            words = {
                "a" + "".join(rng.choice("abc") for _ in range(8)) + "b"
                for _ in range(20)
            }
        add(words=sorted(words))
    assert len(calls) == 600
    return calls
