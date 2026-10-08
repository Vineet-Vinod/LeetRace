import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    valid = [chr(code) for code in range(33, 123) if chr(code) not in {'"', "\\"}]
    while len(calls) < 600:
        s = "".join(rng.choices(valid, k=rng.randint(1, 100)))
        calls.add(f"candidate(s={s!r})")
    return sorted(calls)
