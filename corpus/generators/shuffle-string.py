import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        size = rng.randint(1, 100)
        s = "".join(rng.choices(string.ascii_lowercase, k=size))
        indices = list(range(size))
        rng.shuffle(indices)
        assert sorted(indices) == list(range(size))
        calls.add(f"candidate(s={s!r}, indices={indices!r})")
    return sorted(calls)
