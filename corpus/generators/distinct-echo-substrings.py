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
        assert 1 <= len(d["text"]) <= 2000 and letters(d["text"])

    add(text="abcabcabc")
    add(text="leetcodeleetcode")
    add(text="a" * 2000)
    add(text=("abcdefghijklmnopqrstuvwxyz" * 77)[:2000])
    while len(calls) < 600:
        base = "".join(rng.choice("abcde") for _ in range(rng.randint(1, 24)))
        text = (
            base * rng.randint(2, 5)
            if rng.randrange(2)
            else "".join(
                rng.choice("abcdefghijklmnopqrstuvwxyz")
                for _ in range(rng.randint(1, 80))
            )
        )
        add(text=text)
    assert len(calls) == 600
    return calls
