import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        s, sub, m = kw["s"], kw["sub"], kw["mappings"]
        chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        assert 1 <= len(sub) <= len(s) <= 5000 and set(s) <= chars and set(sub) <= chars
        assert len(m) <= 1000 and all(
            len(v) == 2 and v[0] != v[1] and set(v) <= chars for v in m
        )
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kw.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for kw in [
        {
            "s": "fool3e7bar",
            "sub": "leet",
            "mappings": [["e", "3"], ["t", "7"], ["t", "8"]],
        },
        {"s": "fooleetbar", "sub": "f00l", "mappings": [["o", "0"]]},
        {
            "s": "Fool33tbaR",
            "sub": "leetd",
            "mappings": [["e", "3"], ["t", "7"], ["t", "8"], ["d", "b"], ["p", "b"]],
        },
    ] + [
        {"s": "a" * 5000, "sub": "b" * 5000, "mappings": [["b", "a"]] * 1000},
        {"s": "a" * 5000, "sub": "b" * 4999, "mappings": []},
        {"s": "c", "sub": "a", "mappings": [["a", "b"], ["b", "c"]]},
    ]:
        add(**kw)
    chars = "abcABC012"
    while len(calls) < 600:
        n = rng.randint(1, 50)
        sub_length = rng.randint(1, n)
        sub = "".join(rng.choice(chars) for _ in range(sub_length))
        mappings = [rng.sample(chars, 2) for _ in range(rng.randint(0, 20))]
        s = "".join(rng.choice(chars) for _ in range(n))
        if len(calls) % 2 == 0:
            allowed = {c: [c] for c in chars}
            for a, b in mappings:
                allowed[a].append(b)
            replacement = "".join(rng.choice(allowed[c]) for c in sub)
            start = rng.randint(0, n - sub_length)
            s = s[:start] + replacement + s[start + sub_length :]
        add(s=s, sub=sub, mappings=mappings)
    return calls
