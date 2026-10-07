import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        "Leetcode is cool",
        "Keep calm and code on",
        "To be or not to be",
        "A",
        "A " + "b" * 99_997,
    }
    while len(cases) < 600:
        words = [
            "".join(
                rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, 12))
            )
            for _ in range(rng.randint(1, 20))
        ]
        sentence = " ".join(words)
        cases.add(sentence[0].upper() + sentence[1:])
    assert all(
        1 <= len(text) <= 100_000
        and text[0].isupper()
        and all(word.islower() for word in text.split()[1:])
        and "  " not in text
        for text in cases
    )
    return [f"candidate(text={text!r})" for text in sorted(cases)]
