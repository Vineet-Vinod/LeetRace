import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    while len(calls) < 600:
        s = "".join(rng.choices(alphabet, k=rng.randint(1, 100)))
        if rng.randrange(2):
            shift = rng.randrange(len(s))
            goal = s[shift:] + s[:shift]
        else:
            goal = "".join(rng.choices(alphabet, k=rng.randint(1, 100)))
        calls.add(f"candidate(s={s!r}, goal={goal!r})")
    return sorted(calls)
