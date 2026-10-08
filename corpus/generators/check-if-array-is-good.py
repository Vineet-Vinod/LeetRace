import random


def _is_good(values: list[int]) -> bool:
    maximum = max(values)
    return len(values) == maximum + 1 and sorted(values) == list(
        range(1, maximum + 1)
    ) + [maximum]


def generate(seed: int = 0) -> list[str]:
    """Construct 300 valid permutations and 300 legal counterexamples, within n<=100 and value<=200."""
    rng = random.Random(seed)
    positives = {(1, 1), (1, 3, 3, 2)}
    while len(positives) < 300:
        maximum = rng.randint(1, 99)
        values = list(range(1, maximum + 1)) + [maximum]
        rng.shuffle(values)
        positives.add(tuple(values))

    negatives = {(2, 1, 3), (3, 4, 4, 1, 2, 1), (200,) + tuple(range(1, 100))}
    while len(negatives) < 300:
        length = rng.randint(1, 100)
        values = [rng.randint(1, 200) for _ in range(length)]
        if not _is_good(values):
            negatives.add(tuple(values))

    cases = sorted(positives) + sorted(negatives)
    assert len(cases) == len(set(cases)) == 600
    assert all(1 <= len(values) <= 100 for values in cases)
    assert all(1 <= value <= 200 for values in cases for value in values)
    assert all(_is_good(list(values)) for values in positives)
    assert all(not _is_good(list(values)) for values in negatives)
    return [f"candidate(nums={list(values)!r})" for values in cases]
