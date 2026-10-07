import random
import string
from collections import Counter


def unique_window(s, t):
    # Count minimum windows independently; the original promise is preserved.
    need = Counter(t)
    count = Counter()
    left = 0
    best = len(s) + 1
    ways = 0
    missing = len(t)
    for right, c in enumerate(s):
        count[c] += 1
        if count[c] <= need[c]:
            missing -= 1
        while not missing:
            length = right - left + 1
            if length < best:
                best, ways = length, 1
            elif length == best:
                ways += 1
            c = s[left]
            count[c] -= 1
            if count[c] < need[c]:
                missing += 1
            left += 1
    return ways <= 1


def sample(r, turn):
    n = r.randint(1, 40)
    s = "".join(r.choices("abAB", k=n))
    t = "".join(r.choices("abABz", k=r.randint(1, 12)))
    if turn % 2 == 0:
        start = r.randrange(n)
        t = s[start : min(n, start + r.randint(1, 8))]
    return dict(s=s, t=t)


def validate(s, t):
    assert 1 <= len(s) <= 100000 and 1 <= len(t) <= 100000
    assert all(c in string.ascii_letters for c in s + t)
    assert unique_window(s, t)


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

    add(s="ADOBECODEBANC", t="ABC")
    add(s="a", t="a")
    add(s="a", t="aa")
    add(s="A" * 99999 + "B", t="A" * 99999 + "B")
    add(s="A" * 100000, t="B")
    turn = 0
    while len(calls) < 600:
        kwargs = sample(r, turn)
        turn += 1
        if not unique_window(kwargs["s"], kwargs["t"]):
            continue
        add(**kwargs)
    assert len(calls) == len(set(calls)) == 600
    return calls
