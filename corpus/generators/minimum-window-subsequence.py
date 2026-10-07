import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        a, b = kw["s1"], kw["s2"]
        assert 1 <= len(a) <= 20000 and 1 <= len(b) <= 100
        assert all(s.isascii() and s.islower() and s.isalpha() for s in (a, b))
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kw.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for kw in [
        {"s1": "abcdebdde", "s2": "bde"},
        {"s1": "jmeqksfrsdcmsiwvaovztaqenprpvnbstl", "s2": "u"},
    ] + [
        {"s1": "a" * 20000, "s2": "a" * 100},
        {"s1": "abcde" * 4000, "s2": "edcba" * 20},
        {"s1": "a", "s2": "a" * 100},
    ]:
        add(**kw)
    while len(calls) < 600:
        n = rng.randint(1, 80)
        a = "".join(rng.choice("abcde") for _ in range(n))
        if len(calls) % 3 == 0:
            indices = sorted(rng.sample(range(n), rng.randint(1, min(n, 10))))
            b = "".join(a[i] for i in indices)
        elif len(calls) % 3 == 1:
            b = "z" + "".join(rng.choice("abcd") for _ in range(rng.randint(0, 10)))
        else:
            b = "".join(rng.choice("abcde") for _ in range(rng.randint(1, 12)))
        add(s1=a, s2=b)
    return calls
