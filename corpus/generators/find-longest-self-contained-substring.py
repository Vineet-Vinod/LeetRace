import random
import string

EXAMPLES = ["candidate(s='abba')", "candidate(s='abab')", "candidate(s='abacd')"]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = list(EXAMPLES)
    seen = set(calls)

    def emit(call: str) -> None:
        if call not in seen:
            calls.append(call)
            seen.add(call)

    def add(s):
        assert 2 <= len(s) <= 50000 and set(s) <= set(string.ascii_lowercase)
        emit(f"candidate(s={s!r})")

    add("a" * 50000)
    add("a" * 49999 + "b")
    add("abcdefghijklmnopqrstuvwxyz" * 1923 + "ab")
    while len(calls) < 600:
        n = rng.randint(2, 80)
        family = rng.randrange(3)
        if family == 0:
            # Disjoint alphabets create long proper self-contained pieces.
            split = rng.randint(1, n - 1)
            s = "".join(rng.choices("abc", k=split)) + "".join(
                rng.choices("def", k=n - split)
            )
        elif family == 1:
            half = "".join(rng.choices("abcde", k=max(1, n // 2)))
            s = half + half
        else:
            s = "".join(rng.choices("abcdef", k=n))
        add(s)
    return calls
