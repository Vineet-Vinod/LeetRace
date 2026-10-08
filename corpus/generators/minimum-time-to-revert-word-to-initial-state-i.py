import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[str, int]] = {
        ("abacaba", 3),
        ("abacaba", 4),
        ("abcbabcd", 2),
        ("a", 1),
        ("a" * 50, 1),
        ("ab" * 25, 2),
    }
    alphabet = string.ascii_lowercase[:6]
    while len(cases) < 600:
        word = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 50)))
        cases.add((word, rng.randint(1, len(word))))
    assert all(
        1 <= len(word) <= 50
        and 1 <= k <= len(word)
        and set(word) <= set(string.ascii_lowercase)
        for word, k in cases
    )
    return [f"candidate(word={word!r}, k={k})" for word, k in sorted(cases)]
