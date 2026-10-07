import random


def sample(r, turn):
    n = r.randint(1, 55)
    k = r.randint(1, n)
    if turn % 3 == 0:
        k = r.randint(1, 6)
        word = "".join(c * k for c in r.choices("abcd", k=r.randint(1, 8)))
    else:
        word = "".join(
            r.choices(r.choice(["abc", "az", "abcdefghijklmnopqrstuvwxyz"]), k=n)
        )
    return dict(word=word, k=k)


def validate(word, k):
    assert (
        1 <= len(word) <= 100000
        and word.isascii()
        and word.islower()
        and word.isalpha()
        and 1 <= k <= len(word)
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

    add(word="igigee", k=2)
    add(word="aaabbbccc", k=3)
    add(word="a" * 100000, k=1)
    add(word="az" * 50000, k=100000)
    turn = 0
    while len(calls) < 600:
        kwargs = sample(r, turn)
        turn += 1
        add(**kwargs)
    assert len(calls) == len(set(calls)) == 600
    return calls
