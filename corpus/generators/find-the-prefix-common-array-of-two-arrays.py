import random


def generate(seed: int = 0) -> list[str]:
    """A and B are independently shuffled permutations of the same set 1..n."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        n = 1 + i % 60
        A = list(range(1, n + 1))
        B = A.copy()
        rng.shuffle(A)
        rng.shuffle(B)
        assert sorted(A) == sorted(B) == list(range(1, n + 1))
        call = f"candidate(A={A!r}, B={B!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
