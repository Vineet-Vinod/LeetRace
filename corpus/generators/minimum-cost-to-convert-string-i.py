import random
import string


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: source/target equal length1..10^5; 1..2000 valid differing lowercase conversion rules with positive costs<=10^6."""
    rng = random.Random(seed)
    calls = {
        "candidate(source='abcd', target='acbe', original=['a', 'b', 'c', 'c', 'e', 'd'], changed=['b', 'c', 'b', 'e', 'b', 'e'], cost=[2, 5, 5, 1, 2, 20])"
    }
    while len(calls) < 600:
        source = "".join(
            rng.choice(string.ascii_lowercase[:8]) for _ in range(rng.randint(1, 100))
        )
        target = "".join(
            rng.choice(string.ascii_lowercase[:8]) for _ in range(len(source))
        )
        count = rng.randint(1, 60)
        original, changed = [], []
        for _ in range(count):
            first = rng.choice(string.ascii_lowercase[:8])
            second = rng.choice(string.ascii_lowercase[:8].replace(first, ""))
            original.append(first)
            changed.append(second)
        costs = [rng.randint(1, 1000) for _ in range(count)]
        calls.add(
            f"candidate(source={source!r}, target={target!r}, original={original!r}, changed={changed!r}, cost={costs!r})"
        )
    return sorted(calls)
