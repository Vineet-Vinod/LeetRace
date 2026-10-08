import random


def generate(seed: int = 0) -> list[str]:
    r = random.Random(seed)
    cases = []
    seen = set()

    def add(s):
        if s not in seen:
            assert 1 <= len(s) <= 1000 and set(s) <= {"0", "1"}
            seen.add(s)
            cases.append(f"candidate(s={s!r})")

    add("0")
    add("1")
    add("01")
    add("10")
    add("1110")
    add("111")
    for _ in range(300):
        n = r.randint(2, 1000)
        z = (n + 1) // 2
        o = n // 2
        bits = ["0"] * z + ["1"] * o
        r.shuffle(bits)
        add("".join(bits))
    for _ in range(300):
        n = r.randint(2, 1000)
        z = r.randint(0, n)
        o = n - z
        if abs(z - o) <= 1:
            z = min(n, z + 2)
            o = n - z
        add("0" * z + "1" * o)
    add("0" * 500 + "1" * 500)
    add("0" * 501 + "1" * 499)
    add("0" * 502 + "1" * 498)
    return cases
