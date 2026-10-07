import random

DOMAIN_SIZE = 38


def generate(seed: int = 0) -> list[str]:
    random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        assert 1 <= kw["n"] <= 4 and 1 <= kw["k"] <= 10 and kw["k"] ** kw["n"] <= 4096
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kw.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for kw in [{"n": 1, "k": 2}, {"n": 2, "k": 2}] + []:
        add(**kw)
    for n in range(1, 5):
        for k in range(1, 11):
            if k**n <= 4096:
                add(n=n, k=k)
    return calls
