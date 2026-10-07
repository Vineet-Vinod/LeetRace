import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = {
        "a",
        "ababa",
        "aaabaaa",
        "a" * 20_000,
        "a" * 9_999 + "b" + "a" * 10_000,
        string.ascii_lowercase,
    }
    while len(cases) < 600:
        size = rng.randint(1, 80)
        alphabet = rng.randint(1, min(8, size))
        if rng.random() < 0.55:
            char = rng.choice(string.ascii_lowercase)
            text = char * rng.randint(1, size)
            text += "".join(
                rng.choice(string.ascii_lowercase.replace(char, ""))
                for _ in range(size - len(text))
            )
            text = "".join(rng.sample(list(text), len(text)))
        else:
            text = "".join(
                rng.choice(string.ascii_lowercase[:alphabet]) for _ in range(size)
            )
        cases.add(text)
    assert all(
        1 <= len(text) <= 20_000 and all("a" <= char <= "z" for char in text)
        for text in cases
    )
    return [f"candidate(text={text!r})" for text in sorted(cases)]
