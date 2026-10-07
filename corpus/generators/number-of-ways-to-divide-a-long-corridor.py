import random


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
        assert 1 <= len(d["corridor"]) <= 100000 and set(d["corridor"]) <= set("SP")

    add(corridor="SSPPSPS")
    add(corridor="PPSPSP")
    add(corridor="S")
    add(corridor="P" * 100000)
    add(corridor="S" * 100000)
    add(corridor="SP" * 50000)
    while len(calls) < 600:
        n = rng.randint(1, 150)
        s = "".join(rng.choice("SP") for _ in range(n))
        # Half of random cases deliberately have a positive even seat count.
        if rng.randrange(2):
            positions = (
                rng.sample(range(n), rng.randrange(1, n // 2 + 1) * 2) if n >= 2 else []
            )
            s = "".join("S" if i in positions else "P" for i in range(n))
        add(corridor=s)
    assert len(calls) == 600
    return calls
