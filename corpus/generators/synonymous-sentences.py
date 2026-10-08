def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(synonyms=[['happy', 'joy'], ['sad', 'sorrow'], ['joy', 'cheerful']], text='I am happy today but was sad yesterday')",
        "candidate(synonyms=[], text='hello there')",
    }
    words = ["aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "ii", "jj"]
    while len(cases) < 600:
        pool = rng.sample(words, rng.randint(0, 10))
        pairs = []
        for i in range(1, len(pool)):
            if rng.random() < 0.5:
                pairs.append([pool[i - 1], pool[i]])
        text_words = [
            rng.choice(words + ["outside"]) for _ in range(rng.randint(1, 10))
        ]
        assert (
            len(pairs) <= 10
            and len(text_words) <= 10
            and len({tuple(sorted(p)) for p in pairs}) == len(pairs)
        )
        cases.add(f"candidate(synonyms={pairs!r}, text={' '.join(text_words)!r})")
    return sorted(cases)
