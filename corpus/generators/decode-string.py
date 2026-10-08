def _generate_base(seed: int = 0) -> list[str]:
    import random
    import string

    rng = random.Random(seed)
    cases = {"candidate(s='3[a]2[bc]')", "candidate(s='3[a2[c]]')"}
    for _ in range(598):
        pieces = []
        for _ in range(rng.randint(1, 3)):
            letter = rng.choice(string.ascii_lowercase)
            repeat = rng.randint(1, 9)
            if rng.random() < 0.25:
                inner = rng.choice(string.ascii_lowercase) + rng.choice(
                    string.ascii_lowercase
                )
                pieces.append(f"{repeat}[2[{inner}]]")
            else:
                pieces.append(f"{repeat}[{letter}]")
        encoded = "".join(pieces)
        assert len(encoded) <= 30
        cases.add(f"candidate(s={encoded!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(s={'10[a]' * 6!r})"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
