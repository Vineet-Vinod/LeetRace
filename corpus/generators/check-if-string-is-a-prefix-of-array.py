import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    alphabet = "abc"
    while len(calls) < 600:
        words = [
            "".join(rng.choices(alphabet, k=rng.randint(1, 8)))
            for _ in range(rng.randint(1, 20))
        ]
        if rng.randrange(2):
            take = rng.randint(1, len(words))
            s = "".join(words[:take])
        else:
            s = "".join(rng.choices(alphabet, k=rng.randint(1, 40)))
        calls.add(f"candidate(s={s!r}, words={words!r})")
    return sorted(calls)
