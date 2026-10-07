import random


def possible(a, b):
    def ok(x, y):
        left, right = 0, len(x) - 1
        while left < right and x[left] == y[right]:
            left += 1
            right -= 1
        return (
            x[left : right + 1] == x[left : right + 1][::-1]
            or y[left : right + 1] == y[left : right + 1][::-1]
        )

    return ok(a, b) or ok(b, a)


def generate(seed: int = 0) -> list[str]:
    r = random.Random(seed)
    cases = []
    seen = set()

    def add(a, b):
        if (a, b) not in seen:
            assert 1 <= len(a) == len(b) <= 100_000 and a.islower() and b.islower()
            seen.add((a, b))
            cases.append(f"candidate(a={a!r}, b={b!r})")

    for _ in range(300):
        n = r.randint(1, 100)
        pal = "".join(r.choice("abc") for _ in range(n // 2))
        p = pal + ("x" if n % 2 else "") + pal[::-1]
        cut = r.randint(0, n)
        a = p[:cut] + "".join(r.choice("xyz") for _ in range(n - cut))
        b = "".join(r.choice("uvw") for _ in range(cut)) + p[cut:]
        add(a, b)
    count = 0
    while count < 300:
        n = r.randint(2, 100)
        a = "".join(r.choice("abcdef") for _ in range(n))
        b = "".join(r.choice("ghijkl") for _ in range(n))
        if not possible(a, b):
            add(a, b)
            count += 1
    add("a" * 50_000 + "b" * 50_000, "c" * 50_000 + "a" * 50_000)
    long_a = "a" * 99_999 + "b"
    long_b = "c" * 99_999 + "d"
    if not possible(long_a, long_b):
        add(long_a, long_b)
    return cases
