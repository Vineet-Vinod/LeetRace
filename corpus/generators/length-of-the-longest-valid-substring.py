import random


def sample(r, turn):
    n = r.randint(1, 55)
    word = "".join(r.choices("abcd", k=n))
    f = []
    for _ in range(r.randint(1, 20)):
        if turn % 3 == 0:
            f.append("z" * r.randint(1, 10))
        else:
            a = r.randrange(n)
            f.append(word[a : min(n, a + r.randint(1, 10))])
    if turn % 5 == 0:
        f = list("abcd")
    return dict(word=word, forbidden=f)


def validate(word, forbidden):
    assert (
        1 <= len(word) <= 100000
        and word.isascii()
        and word.isalpha()
        and word.islower()
    )
    assert 1 <= len(forbidden) <= 100000 and all(
        1 <= len(f) <= 10 and f.isascii() and f.isalpha() and f.islower()
        for f in forbidden
    )


def generate(seed: int = 0) -> list[str]:
    r = random.Random(seed)
    calls = []
    seen = set()

    def add(**kwargs):
        validate(**kwargs)
        parts = []
        for key, value in kwargs.items():
            expression = repr(value)
            parts.append(key + "=" + expression)
        call = "candidate(" + ", ".join(parts) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(word="cbaaaabc", forbidden=["aaa", "cb"])
    add(word="leetcode", forbidden=["de", "le", "e"])
    add(word="a" * 100000, forbidden=["a" * 10] * 100000)
    add(word="z" * 100000, forbidden=["a"])
    turn = 0
    while len(calls) < 600:
        kwargs = sample(r, turn)
        turn += 1
        add(**kwargs)
    assert len(calls) == len(set(calls)) == 600
    return calls
