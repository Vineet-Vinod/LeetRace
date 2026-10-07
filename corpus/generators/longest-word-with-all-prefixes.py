def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        words = set()
        n = rng.randint(1, 40)
        for _ in range(n):
            length = rng.randint(1, 12)
            words.add("".join(rng.choice("abcde") for _ in range(length)))
        seed_word = "".join(rng.choice("abcde") for _ in range(rng.randint(1, 12)))
        for length in range(1, len(seed_word) + 1):
            if rng.random() < 0.6:
                words.add(seed_word[:length])
        cases.add(f"candidate(words={sorted(words)!r})")
    return sorted(cases)
