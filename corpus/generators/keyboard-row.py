import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    alphabet = string.ascii_letters
    while len(calls) < 600:
        words = [
            "".join(rng.choices(alphabet, k=rng.randint(1, 100)))
            for _ in range(rng.randint(1, 20))
        ]
        calls.add(f"candidate(words={words!r})")
    return sorted(calls)
