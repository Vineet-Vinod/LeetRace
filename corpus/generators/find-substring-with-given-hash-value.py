import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def valid(d):
        s = d["s"]
        k = d["k"]
        p = d["power"]
        m = d["modulo"]
        h = d["hashValue"]
        assert (
            1 <= k <= len(s) <= 20000
            and all("a" <= c <= "z" for c in s)
            and 1 <= p <= 10**9
            and 1 <= m <= 10**9
            and 0 <= h < m
        )
        # Independently enumerate forward polynomial hashes in linear time using power sums.
        weights = [pow(p, j, m) for j in range(k)]
        if len(s) <= 60:
            assert any(
                sum((ord(c) - 96) * weights[j] for j, c in enumerate(s[i : i + k])) % m
                == h
                for i in range(len(s) - k + 1)
            )
        else:
            assert (
                len(set(s)) == 1 and sum((ord(s[0]) - 96) * v for v in weights) % m == h
            )

    def add(**kwargs):
        valid(kwargs)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(s="leetcode", power=7, modulo=20, k=2, hashValue=0)
    add(s="fbxzaad", power=31, modulo=100, k=3, hashValue=32)
    add(s="z" * 20000, power=10**9, modulo=10**9, k=20000, hashValue=26)
    add(s="a" * 20000, power=1, modulo=1, k=1, hashValue=0)
    t = 0
    while len(calls) < 600:
        n = rng.randint(1, 60)
        s = "".join(rng.choice("abcdefghxyz") for _ in range(n))
        k = rng.randint(1, n)
        p = rng.choice([1, 2, 7, 31, 10**9, rng.randint(1, 10**9)])
        m = rng.choice([1, 2, 20, 100, 10**9, rng.randint(1, 10**9)])
        i = rng.randint(0, n - k)
        h = sum((ord(c) - 96) * pow(p, j, m) for j, c in enumerate(s[i : i + k])) % m
        add(s=s, power=p, modulo=m, k=k, hashValue=h)
        t += 1
    return calls
