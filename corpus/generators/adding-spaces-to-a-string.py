import random
import string


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: string length 1..300000; spaces are unique increasing indices in [0,len(s)-1]."""
    rng = random.Random(seed)
    calls: set[str] = set()
    calls.add("candidate(s='spacing', spaces=[0, 1, 2, 3, 4, 5, 6])")
    calls.add("candidate(s='EnjoyYourCoffee', spaces=[5, 9])")
    while len(calls) < 600:
        size = rng.randint(1, 100)
        s = "".join(rng.choice(string.ascii_letters) for _ in range(size))
        positions = sorted(rng.sample(range(size), rng.randint(1, size)))
        calls.add(f"candidate(s={s!r}, spaces={positions!r})")
    return sorted(calls)
