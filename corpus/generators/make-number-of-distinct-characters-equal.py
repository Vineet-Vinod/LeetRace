import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {("ac", "b"), ("abcc", "aab"), ("abcde", "fghij"), ("a", "a")}
    cases.add(("a" * 100_000, "b" * 100_000))
    alphabet = string.ascii_lowercase[:8]
    while len(cases) < 600:
        first = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 50)))
        second = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 50)))
        cases.add((first, second))
    assert all(
        1 <= len(first) <= 100_000
        and 1 <= len(second) <= 100_000
        and set(first) <= set(string.ascii_lowercase)
        and set(second) <= set(string.ascii_lowercase)
        for first, second in cases
    )
    return [
        f"candidate(word1={first!r}, word2={second!r})"
        for first, second in sorted(cases)
    ]
