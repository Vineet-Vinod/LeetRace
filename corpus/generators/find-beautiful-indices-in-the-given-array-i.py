def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases: set[str] = set()

    def add(s: str, a: str, b: str, k: int) -> None:
        assert 1 <= len(s) <= 100_000
        assert 1 <= len(a) <= 10 and 1 <= len(b) <= 10
        assert 1 <= k <= len(s)
        assert all("a" <= char <= "z" for char in s + a + b)
        cases.add(f"candidate(s={s!r}, a={a!r}, b={b!r}, k={k})")

    add("isawsquirrelnearmysquirrelhouseohmy", "my", "squirrel", 15)
    add("a" + "x" * 99_998 + "b", "a", "b", 100_000)

    # Every positive case places one a and b occurrence within distance k.
    for index in range(300):
        a = "".join(rng.choice("abc") for _ in range(1 + index % 10))
        b = "".join(rng.choice("xyz") for _ in range(1 + (index * 7) % 10))
        gap = rng.randint(0, 100)
        prefix = "r" * (index % 100)
        s = prefix + a + "q" * gap + b
        add(s, a, b, max(1, len(a) + gap))

    # These strings have neither requested substring and guarantee empty output.
    for index in range(300):
        s = "c" * (1 + index % 100)
        a = "a" * (1 + index % 10)
        b = "b" * (1 + (index * 3) % 10)
        add(s, a, b, rng.randint(1, len(s)))

    while len(cases) < 600:
        size = rng.randint(1, 1000)
        s = "".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(size))
        a = "".join(
            rng.choice("abcdefghijklmnopqrstuvwxyz")
            for _ in range(rng.randint(1, min(10, size)))
        )
        b = "".join(
            rng.choice("abcdefghijklmnopqrstuvwxyz")
            for _ in range(rng.randint(1, min(10, size)))
        )
        add(s, a, b, rng.randint(1, size))

    result = list(cases)
    rng.shuffle(result)
    return result
