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
        array(d["nums"], 1, 100000, 100000)

    add(nums=[100000] * 100000)
    add(nums=[1] * 100000)
    add(nums=list(range(1, 100001)))
    add(nums=[2, 5, 9])
    add(nums=[7] * 7)
    while len(calls) < 600:
        add(
            nums=[
                rng.randint(1, 100000 if rng.randrange(5) == 0 else 100)
                for _ in range(rng.randint(1, 80))
            ]
        )
    assert len(calls) == 600
    return calls
