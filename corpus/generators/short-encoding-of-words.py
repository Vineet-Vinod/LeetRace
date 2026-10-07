def generate(seed: int = 0) -> list[str]:
    import random
    import string

    rng = random.Random(seed)
    cases = {
        "candidate(words=['time', 'me', 'bell'])",
        "candidate(words=['t'])",
        "candidate(words=['time', 'atime', 'btime'])",
        "candidate(words=['me', 'time', 'ime'])",
        "candidate(words=['abc', 'bc', 'c'])",
        "candidate(words=['time', 'time', 'time'])",
        "candidate(words=['abc', 'def', 'ghi'])",
        "candidate(words=['hello', 'ello', 'llo', 'lo', 'o'])",
        f"candidate(words={['a' * i for i in range(1, 8)]!r})",
        f"candidate(words={['word'] * 2000!r})",
    }
    alphabet = string.ascii_lowercase
    while len(cases) < 600:
        words = [
            "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 7)))
            for _ in range(rng.randint(1, 2000))
        ]
        if rng.random() < 0.4 and words:
            base = words[0]
            words.extend(base[index:] for index in range(1, len(base)))
        assert 1 <= len(words) <= 2000
        assert all(1 <= len(word) <= 7 and word.islower() for word in words)
        cases.add(f"candidate(words={words!r})")
    return sorted(cases)
