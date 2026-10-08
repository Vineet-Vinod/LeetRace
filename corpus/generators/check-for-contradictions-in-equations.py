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
        equations, values = d["equations"], d["values"]
        assert 1 <= len(equations) <= 100 and len(equations) == len(values)
        assert all(
            len(pair) == 2 and all(1 <= len(x) <= 5 and letters(x) for x in pair)
            for pair in equations
        )
        assert all(0 < v <= 10 and abs(v * 100 - round(v * 100)) < 1e-8 for v in values)
        # Ratios are exact powers of two or short cent values. Contradictory edges
        # differ by at least .01, avoiding precision-targeted cases.

    add(equations=[["a", "b"], ["b", "c"], ["a", "c"]], values=[3, 0.5, 1.5])
    add(equations=[["a", "a"]], values=[0.01])
    add(equations=[["abcde", "abcde"]], values=[10.0])
    add(equations=[["a", "b"]] * 100, values=[1.0] * 100)
    while len(calls) < 600:
        n = rng.randint(2, 12)
        names = [chr(97 + i) for i in range(n)]
        weights = [2 ** rng.randint(0, 2) for _ in names]
        equations = []
        values = []
        for _ in range(rng.randint(1, 60)):
            a, b = rng.randrange(n), rng.randrange(n)
            equations.append([names[a], names[b]])
            values.append(weights[a] / weights[b])
        if rng.randrange(2):
            equations.append(equations[0][:])
            values.append(values[0] + 0.25)
        add(equations=equations, values=values)
    assert len(calls) == 600
    return calls
