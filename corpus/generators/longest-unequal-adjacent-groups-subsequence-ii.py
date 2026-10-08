def generate(seed: int = 0) -> list[str]:
    import random
    import string

    rng = random.Random(seed)
    letters = string.ascii_lowercase[:8]
    cases = {
        "candidate(words=['bab', 'dab', 'cab'], groups=[1, 2, 2])",
        "candidate(words=['a', 'b', 'c', 'd'], groups=[1, 2, 3, 4])",
    }

    def gray_words(size: int) -> list[str]:
        width = max(1, (size - 1).bit_length())
        return [
            format(index ^ (index >> 1), f"0{width}b").translate(
                str.maketrans("01", "ab")
            )
            for index in range(size)
        ]

    boundary_words = gray_words(1000)
    boundary_groups = [index % 2 + 1 for index in range(1000)]
    cases.add(f"candidate(words={boundary_words!r}, groups={boundary_groups!r})")
    while len(cases) < 600:
        size = rng.randint(1, 60)
        values = []
        seen = set()
        while len(values) < size:
            word = "".join(rng.choice(letters) for _ in range(rng.randint(1, 8)))
            if word not in seen:
                seen.add(word)
                values.append(word)
        groups = [rng.randint(1, size) for _ in range(size)]
        assert len(values) == len(groups) and len(set(values)) == size
        assert all(1 <= group <= size for group in groups)
        cases.add(f"candidate(words={values!r}, groups={groups!r})")
    assert len(cases) == 600
    return sorted(cases)
