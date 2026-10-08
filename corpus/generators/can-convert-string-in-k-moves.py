import random


def generate(seed: int = 0) -> list[str]:
    r = random.Random(seed)
    cases = []
    seen = set()

    def add(s, t, k):
        key = (s, t, k)
        if key not in seen:
            assert 1 <= len(s) == len(t) <= 100_000 and 0 <= k <= 10**9
            assert s.islower() and t.islower()
            seen.add(key)
            cases.append(f"candidate(s={s!r}, t={t!r}, k={k})")

    add("a", "a", 0)
    add("a", "b", 1)
    add("a", "c", 1)
    add("a", "z", 25)
    for i in range(300):
        n = r.randint(1, 100)
        s = "".join(r.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(n))
        # The identity mapping is always possible; random shifts test scheduling too.
        if i % 2:
            t = s
            k = 0
        else:
            t = "".join(chr((ord(c) - 97 + 1) % 26 + 97) for c in s)
            k = 10**6
        add(s, t, k)
    for _ in range(300):
        n = r.randint(1, 100)
        s = "".join(r.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(n))
        t = "".join(r.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(n))
        add(s, t, 0)
    add("a" * 100_000, "b" * 100_000, 10**9)
    add("a" * 100_000, "b" * 100_000, 1)
    return cases
