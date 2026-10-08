import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = {f"candidate(s={'ID' * 50000!r})"}
    while len(calls) < 600:
        size = rng.randint(1, 1000)
        s = "".join(rng.choice("ID") for _ in range(size))
        calls.add(f"candidate(s={s!r})")
    return sorted(calls)
