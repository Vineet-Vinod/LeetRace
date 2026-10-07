def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    alphabet = "aeioubcdfgXYZ"
    cases = {
        "candidate(wordlist=['KiTe','kite','hare','Hare'], queries=['kite','Kite','KiTe','Hare','HARE','Hear','hear','keti','keet','keto'])",
        "candidate(wordlist=['yellow'], queries=['YellOw'])",
    }
    while len(cases) < 600:
        words = [
            "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 7)))
            for _ in range(rng.randint(1, 20))
        ]
        queries = [
            "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 7)))
            for _ in range(rng.randint(1, 20))
        ]
        assert (
            1 <= len(words) <= 5000
            and 1 <= len(queries) <= 5000
            and all(1 <= len(w) <= 7 for w in words + queries)
        )
        cases.add(f"candidate(wordlist={words!r}, queries={queries!r})")
    return sorted(cases)
