import random
from collections import Counter


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        s1, s2 = kwargs["s1"], kwargs["s2"]
        assert (
            1 <= len(s1) <= 20
            and Counter(s1) == Counter(s2)
            and set(s1) <= set("abcdef")
        )
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(s1="a" * 10 + "b" * 10, s2="b" * 10 + "a" * 10)
    add(s1="abcdefabcdefabcdefab", s2="abcdefabcdefabcdefab")
    add(s1="ab", s2="ba")
    add(s1="abc", s2="bca")
    while len(calls) < 600:
        n = rng.randint(1, 10)
        s1 = "".join(rng.choices("abcdef", k=n))
        chars = list(s1)
        rng.shuffle(chars)
        s2 = "".join(chars)
        add(s1=s1, s2=s2)
    return calls
