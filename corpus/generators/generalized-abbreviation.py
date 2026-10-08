import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    alphabet = string.ascii_lowercase[:6]
    while len(cases) < 600:
        word = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 8)))
        if word not in seen:
            seen.add(word)
            assert 1 <= len(word) <= 15 and word.islower() and word.isalpha()
            cases.append(f"candidate(word={word!r})")
    return cases
