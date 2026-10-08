import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        ("abcd", "bccda"),
        ("ab", "cd"),
        ("a", "a"),
        ("abc", "cba"),
        ("a" * 2000, "a" * 2000),
        ("a" * 200_000, "a" * 200_000),
    }
    alphabet = string.ascii_lowercase[:6]
    while len(cases) < 600:
        first = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 100)))
        second = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 100)))
        cases.add((first, second))
    assert all(
        1 <= len(first) <= 200_000
        and 1 <= len(second) <= 200_000
        and set(first) <= set(string.ascii_lowercase)
        and set(second) <= set(string.ascii_lowercase)
        for first, second in cases
    )
    return [
        f"candidate(firstString={first!r}, secondString={second!r})"
        for first, second in sorted(cases)
    ]
