import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[str, str]] = {
        ("leetcode", "coats"),
        ("night", "thing"),
        ("a", "a"),
        ("a", "b"),
    }
    cases.add(("a" * 200_000, "a" * 200_000))
    alphabet = string.ascii_lowercase[:8]
    while len(cases) < 600:
        left = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 100)))
        right = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 100)))
        cases.add((left, right))
    assert all(
        1 <= len(left) <= 200_000
        and 1 <= len(right) <= 200_000
        and set(left) <= set(string.ascii_lowercase)
        and set(right) <= set(string.ascii_lowercase)
        for left, right in cases
    )
    return [f"candidate(s={left!r}, t={right!r})" for left, right in sorted(cases)]
