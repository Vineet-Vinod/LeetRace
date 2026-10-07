import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def valid(d):
        a = d["a"]
        b = d["b"]
        assert (
            1 <= len(a) <= 100000
            and 1 <= len(b) <= 100000
            and a == sorted(a)
            and b == sorted(b)
            and len(set(a + b)) == len(a) + len(b)
        )
        assert (
            all(word and all("a" <= c <= "z" for c in word) for word in a + b)
            and sum(map(len, a + b)) <= 10**6
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

    add(a=["avokado", "dabar"], b=["brazil"])
    add(a=["ananas", "atlas", "banana"], b=["albatros", "cikla", "nogomet"])
    add(a=["hrvatska", "zastava"], b=["bijeli", "galeb"])

    def word(i):
        chars = []
        for _ in range(5):
            chars.append(chr(97 + i % 26))
            i //= 26
        return "".join(reversed(chars))

    add(a=[word(i) for i in range(100000)], b=[word(i) for i in range(100000, 200000)])
    add(a=["a" * 500000], b=["b" * 500000])
    t = 0
    while len(calls) < 600:
        n, m = rng.randint(1, 20), rng.randint(1, 20)
        words = set()
        while len(words) < n + m:
            words.add(
                "".join(rng.choice("abcdefxyz") for _ in range(rng.randint(1, 8)))
            )
        words = sorted(words)
        rng.shuffle(words)
        add(a=sorted(words[:n]), b=sorted(words[n:]))
        t += 1
    return calls
