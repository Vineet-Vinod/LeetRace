import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    alphabet = string.ascii_lowercase[:6]
    while len(cases) < 600:
        k = rng.randint(1, 12)
        blocks = rng.randint(1, 20)
        word = "".join(rng.choice(alphabet) for _ in range(k * blocks))
        key = (word, k)
        if key not in seen:
            seen.add(key)
            assert len(word) % k == 0 and word.islower() and word.isalpha()
            cases.append(f"candidate(word={word!r}, k={k})")
    return cases
