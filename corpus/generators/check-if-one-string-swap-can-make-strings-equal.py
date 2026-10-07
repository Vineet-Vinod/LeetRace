import random
import string


def _can_swap(first: str, second: str) -> bool:
    differences = [(left, right) for left, right in zip(first, second) if left != right]
    if not differences:
        return True
    return len(differences) == 2 and differences[0] == differences[1][::-1]


def generate(seed: int = 0) -> list[str]:
    """Generate 300 valid true pairs and 300 false pairs over lowercase strings of length 1..100."""
    rng = random.Random(seed)
    positives = {("bank", "kanb"), ("kelb", "kelb"), ("a" * 100, "a" * 100)}
    while len(positives) < 300:
        first = "".join(
            rng.choice(string.ascii_lowercase) for _ in range(rng.randint(2, 100))
        )
        chars = list(first)
        left, right = rng.sample(range(len(chars)), 2)
        chars[left], chars[right] = chars[right], chars[left]
        positives.add((first, "".join(chars)))

    negatives = {("attack", "defend"), ("abcd", "badc"), ("a" * 100, "b" * 100)}
    while len(negatives) < 300:
        length = rng.randint(1, 100)
        first = "".join(rng.choice(string.ascii_lowercase) for _ in range(length))
        second = "".join(rng.choice(string.ascii_lowercase) for _ in range(length))
        if not _can_swap(first, second):
            negatives.add((first, second))

    pairs = sorted(positives) + sorted(negatives)
    assert len(pairs) == len(set(pairs)) == 600
    assert all(1 <= len(first) == len(second) <= 100 for first, second in pairs)
    assert all(
        set(first + second) <= set(string.ascii_lowercase) for first, second in pairs
    )
    assert all(_can_swap(first, second) for first, second in positives)
    assert all(not _can_swap(first, second) for first, second in negatives)
    return [f"candidate(s1={first!r}, s2={second!r})" for first, second in pairs]
