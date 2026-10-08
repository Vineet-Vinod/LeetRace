import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {"the sky is blue", "  hello world  ", "a good   example"}
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    while len(cases) < 600:
        words = [
            "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 12)))
            for _ in range(rng.randint(1, 20))
        ]
        separator = " " * rng.randint(1, 5)
        text = separator.join(words)
        if rng.random() < 0.5:
            text = " " * rng.randint(0, 5) + text
        if rng.random() < 0.5:
            text += " " * rng.randint(0, 5)
        cases.add(text)
    return [f"candidate(s={s!r})" for s in cases]
