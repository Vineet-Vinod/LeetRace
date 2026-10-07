import random


def generate(seed: int = 0) -> list[str]:
    """Construct 300 monotone and 300 non-monotone strings, each of length 1..100."""
    rng = random.Random(seed)
    positives = {"a", "b", "ab", "aaabbb", "bbb"}
    negatives = {"ba", "abab"}

    while len(positives) < 300:
        length = rng.randint(1, 100)
        split = rng.randint(0, length)
        positives.add("a" * split + "b" * (length - split))

    while len(negatives) < 300:
        length = rng.randint(2, 100)
        chars = [rng.choice("ab") for _ in range(length)]
        position = rng.randrange(length - 1)
        chars[position : position + 2] = ["b", "a"]
        negatives.add("".join(chars))

    cases = sorted(positives) + sorted(negatives)
    assert len(cases) == len(set(cases)) == 600
    assert all(1 <= len(case) <= 100 for case in cases)
    assert all("ba" not in case for case in positives)
    assert all("ba" in case for case in negatives)
    return [f"candidate(s={case!r})" for case in cases]
