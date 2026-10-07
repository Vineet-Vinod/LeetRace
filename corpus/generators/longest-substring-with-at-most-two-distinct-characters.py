import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {"eceba", "ccaabbb", "a", "ab", "abc", "a" * 1000, "ab" * 500}
    cases.add("a" * 100_000)
    alphabet = string.ascii_lowercase
    while len(cases) < 600:
        cases.add("".join(rng.choice(alphabet[:8]) for _ in range(rng.randint(1, 100))))
    assert all(
        1 <= len(value) <= 100_000 and set(value) <= set(alphabet) for value in cases
    )
    return [f"candidate(s={value!r})" for value in sorted(cases)]
