import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**data) -> None:
        s, w = data["s"], data["words"]
        assert 1 <= len(s) <= 10000 and 1 <= len(w) <= 5000 and 1 <= len(w[0]) <= 30
        assert all(len(x) == len(w[0]) for x in w) and all(
            set(x) <= set("abcdefghijklmnopqrstuvwxyz") for x in [s] + w
        )
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in data.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for example in [
        {"s": "barfoothefoobarman", "words": ["foo", "bar"]},
        {"s": "wordgoodgoodgoodbestword", "words": ["word", "good", "best", "word"]},
        {"s": "barfoofoobarthefoobarman", "words": ["bar", "foo", "the"]},
    ]:
        add(**example)
    add(s="a" * 10000, words=["a"] * 5000)
    add(s="a" * 10000, words=["b" * 30] * 5000)
    add(
        s="abcdefghijklmnopqrstuvwxyzaaaa" * 333,
        words=["abcdefghijklmnopqrstuvwxyzaaaa"],
    )
    while len(calls) < 600:
        width = rng.randint(1, 5)
        words = [
            "".join(rng.choice("abc") for _ in range(width))
            for _ in range(rng.randint(1, 8))
        ]
        mode = len(calls) % 3
        if mode == 0:
            ordered = words.copy()
            rng.shuffle(ordered)
            s = "".join(ordered) * rng.randint(1, 3)
            s = "".join(rng.choice("xyz") for _ in range(rng.randint(0, 8))) + s
        elif mode == 1:
            s = "".join(rng.choice("xyz") for _ in range(rng.randint(1, 100)))
        else:
            s = "".join(rng.choice("abc") for _ in range(rng.randint(1, 100)))
        add(s=s, words=words)
    assert len(calls) == 600
    return calls
