import random


def generate(seed: int = 0) -> list[str]:
    """Generate unique nonempty subsequences of a permutation over [1,n]."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        n = 1 + i % 15
        nums = list(range(1, n + 1))
        rng.shuffle(nums)
        sequences = []
        sequence_seen = set()
        for _ in range(1 + i % 20):
            selected = sorted(rng.sample(range(n), 1 + rng.randrange(n)))
            seq = [nums[index] for index in selected]
            key = tuple(seq)
            if key not in sequence_seen:
                sequence_seen.add(key)
                sequences.append(seq)
        call = f"candidate(nums={nums!r}, sequences={sequences!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
