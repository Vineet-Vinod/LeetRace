def generate(seed: int = 0) -> list[str]:
    import random
    import string

    rng = random.Random(seed)
    letters = string.ascii_lowercase
    cases = {
        "candidate(startWords=['ant', 'act', 'tack'], targetWords=['tack', 'act', 'acti'])",
        "candidate(startWords=['ab', 'a'], targetWords=['abc', 'abcd'])",
        "candidate(startWords=['a'], targetWords=['a', 'b', 'aa'])",
        "candidate(startWords=['abcdefghijklmnopqrstuvwxyz'], targetWords=['abcdefghijklmnopqrstuvwxyz'])",
        f"candidate(startWords={['a'] * 50000!r}, targetWords={['ab'] * 50000!r})",
    }
    while len(cases) < 350:
        start = []
        target = []
        for _ in range(rng.randint(1, 20)):
            word = "".join(rng.sample(letters, rng.randint(1, 10)))
            start.append(word)
            if rng.random() < 0.8 and len(word) < 26:
                extra = rng.choice([letter for letter in letters if letter not in word])
                target.append("".join(sorted(word + extra)))
            else:
                target.append("".join(rng.sample(letters, rng.randint(1, 11))))
        assert 1 <= len(start) <= 50000 and 1 <= len(target) <= 50000
        assert all(
            1 <= len(word) <= 26 and len(word) == len(set(word))
            for word in start + target
        )
        cases.add(f"candidate(startWords={start!r}, targetWords={target!r})")

    while len(cases) < 600:
        start = [
            "".join(rng.sample(letters, rng.randint(1, 10)))
            for _ in range(rng.randint(1, 20))
        ]
        target = [
            "".join(rng.sample(letters, rng.randint(1, 11)))
            for _ in range(rng.randint(1, 20))
        ]
        assert all(len(word) == len(set(word)) for word in start + target)
        cases.add(f"candidate(startWords={start!r}, targetWords={target!r})")
    assert len(cases) == 600
    return sorted(cases)
