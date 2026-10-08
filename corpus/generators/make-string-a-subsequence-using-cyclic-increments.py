import random


def generate(seed: int = 0) -> list[str]:
    r = random.Random(seed)
    cases = []
    seen = set()

    def add(a, b):
        if (a, b) not in seen:
            assert 1 <= len(a) <= 100_000 and 1 <= len(b) <= len(a)
            assert a.islower() and b.islower()
            seen.add((a, b))
            cases.append(f"candidate(str1={a!r}, str2={b!r})")

    for _ in range(300):
        n = r.randint(1, 100)
        a = "".join(r.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(n))
        inds = sorted(r.sample(range(n), r.randint(1, n)))
        b = "".join(chr((ord(a[i]) - 97 + r.randrange(2)) % 26 + 97) for i in inds)
        add(a, b)
    for _ in range(300):
        n = r.randint(1, 100)
        m = r.randint(1, n)
        source = "".join(r.choice("abcdefghijklmnopqrstuvwx") for _ in range(n))
        target = "z" + "".join(
            r.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(m - 1)
        )
        add(source, target)
    add("a" * 100_000, "b" * 100_000)
    add("a" * 100_000, "z" * 100_000)
    return cases
