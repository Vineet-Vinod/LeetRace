import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        "babad",
        "cbbd",
        "a",
        "aa",
        "ab",
        "aaaa",
        "abacdfgdcaba",
        "a" * 1000,
        "ab" * 500,
        "0A1A0",
    }
    alphabet = string.ascii_letters + string.digits
    while len(cases) < 600:
        cases.add("".join(rng.choice(alphabet[:8]) for _ in range(rng.randint(1, 80))))
    assert all(
        1 <= len(value) <= 1000 and set(value) <= set(alphabet) for value in cases
    )
    return [f"candidate(s={value!r})" for value in sorted(cases)]
