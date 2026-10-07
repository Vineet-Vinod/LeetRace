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
        assert 1 <= len(d["stamp"]) <= len(d["target"]) <= 1000
        assert letters(d["stamp"]) and letters(d["target"])

    add(stamp="abc", target="ababc")
    add(stamp="abca", target="aabcaca")
    add(stamp="a", target="a" * 1000)
    add(stamp="a" * 1000, target="a" * 1000)
    add(stamp="a", target="b" * 1000)
    while len(calls) < 600:
        stamp = "".join(rng.choice("abc") for _ in range(rng.randint(1, 10)))
        n = rng.randint(len(stamp), 50)
        if rng.randrange(2):
            target = list(stamp * ((n + len(stamp) - 1) // len(stamp)))[:n]
            # Stamp overlapping windows; cover the prefix and suffix last if needed.
            for start in range(0, n - len(stamp) + 1):
                if rng.randrange(2):
                    target[start : start + len(stamp)] = stamp
            target[0 : len(stamp)] = stamp
            target[n - len(stamp) :] = stamp
            target = "".join(target)
        else:
            target = "".join(rng.choice("abcd") for _ in range(n))
        add(stamp=stamp, target=target)
    assert len(calls) == 600
    return calls
