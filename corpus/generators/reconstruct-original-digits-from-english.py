import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    words = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    cases = []
    seen = set()
    while len(cases) < 600:
        digits = "".join(str(rng.randrange(10)) for _ in range(rng.randint(1, 40)))
        s = "".join(words[int(digit)] for digit in digits)
        chars = list(s)
        rng.shuffle(chars)
        scrambled = "".join(chars)
        if scrambled not in seen:
            seen.add(scrambled)
            assert all(c in "egfhionsrutwvxz" for c in scrambled)
            cases.append(f"candidate(s={scrambled!r})")
    return cases
