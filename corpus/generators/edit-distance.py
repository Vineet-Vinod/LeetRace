import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        ("horse", "ros"),
        ("intention", "execution"),
        ("", ""),
        ("a", ""),
        ("a" * 500, "b" * 500),
    }
    alphabet = string.ascii_lowercase[:8]
    while len(cases) < 600:
        first = "".join(rng.choice(alphabet) for _ in range(rng.randint(0, 80)))
        second = "".join(rng.choice(alphabet) for _ in range(rng.randint(0, 80)))
        cases.add((first, second))
    assert all(
        len(first) <= 500
        and len(second) <= 500
        and set(first) <= set(string.ascii_lowercase)
        and set(second) <= set(string.ascii_lowercase)
        for first, second in cases
    )
    return [
        f"candidate(word1={first!r}, word2={second!r})"
        for first, second in sorted(cases)
    ]
