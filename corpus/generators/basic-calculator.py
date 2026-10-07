import random
import re


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
        s = d["s"]
        assert 1 <= len(s) <= 300000
        assert set(s) <= set("0123456789+-() ")
        assert sum(map(int, re.findall(r"\d+", s))) <= 2**31 - 1
        # All expressions are assembled from complete integer terms with optional
        # unary minus at the start of a parenthesis. Bounds on term count and value
        # keep every intermediate calculation inside signed 32-bit integers.

    add(s="1 + 1")
    add(s=" 2-1 + 2 ")
    add(s="(1+(4+5+2)-3)+(6+8)")
    add(s="0" + " " * 299999)
    add(s="(" * 10000 + "1" + ")" * 10000)
    add(s="2147483647")
    add(s="-2147483647")
    add(s="-(1-(2-(3-4)))")
    add(s="1+" * 149999 + "1")
    add(s="(" * 149999 + "1" + ")" * 149999)
    while len(calls) < 600:
        terms = []
        for _ in range(rng.randint(1, 25)):
            values = [rng.randint(0, 10000) for _ in range(rng.randint(1, 6))]
            expr = str(values[0]) + "".join(
                rng.choice([" + ", " - "]) + str(v) for v in values[1:]
            )
            terms.append(("(-" if rng.randrange(3) == 0 else "(") + expr + ")")
        s = terms[0] + "".join(rng.choice([" + ", " - "]) + t for t in terms[1:])
        add(s=s)
    assert len(calls) == 600
    return calls
