def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(sentence='i love leetcode',k=12)"}
    while len(cases) < 600:
        words = [
            "".join(rng.choice("abcde") for _ in range(rng.randint(1, 8)))
            for _ in range(rng.randint(1, 12))
        ]
        sentence = " ".join(words)
        k = rng.randint(max(map(len, words)), 25)
        cases.add(f"candidate(sentence={sentence!r},k={k})")
    return sorted(cases)
