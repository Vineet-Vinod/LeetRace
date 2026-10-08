def _generate_base(seed: int = 0) -> list[str]:
    import random
    import string

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        words = [
            "".join(
                rng.choice(string.ascii_lowercase[:8])
                for _ in range(rng.randint(1, 16))
            )
            for _ in range(rng.randint(1, 50))
        ]
        cases.add(f"candidate(words={words!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    words = [
        "a",
        "ab",
        "abc",
        "abcd",
        "abcde",
        "abcdef",
        "abcdefg",
        "abcdefgh",
        "abcdefghi",
        "abcdefghij",
        "abcdefghijk",
        "abcdefghijkl",
        "abcdefghijklm",
        "abcdefghijklmn",
        "abcdefghijklmno",
        "abcdefghijklmnop",
    ]
    seen = set(words)
    for index in range(26**3):
        value = index
        word = ""
        for _ in range(3):
            word = chr(ord("a") + value % 26) + word
            value //= 26
        if word not in seen:
            words.append(word)
            seen.add(word)
        if len(words) == 1000:
            break
    assert len(words) == len(seen) == 1000
    boundary = f"candidate(words={words!r})"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
