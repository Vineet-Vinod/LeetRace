import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    values = {"a", "a" * 500, "ab" * 250, "abcde" * 100}
    alphabet = string.ascii_lowercase[:6]
    while len(values) < 600:
        value = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 80)))
        values.add(value)
    cases = [f"candidate(s={value!r})" for value in sorted(values)]
    assert len(cases) == len(set(cases)) == 600
    assert all(
        1 <= len(value) <= 500 and value.islower() and value.isalpha()
        for value in values
    )
    return cases
