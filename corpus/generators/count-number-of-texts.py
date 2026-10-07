def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(pressedKeys='22233')",
        "candidate(pressedKeys='222222222222222222222222222222222222')",
    }
    for digit in "2379":
        for length in range(1, 101):
            cases.add(f"candidate(pressedKeys={digit * length!r})")

    while len(cases) < 599:
        if rng.random() < 0.5:
            pressed = "".join(
                rng.choice("23456789") for _ in range(rng.randint(1, 100))
            )
        else:
            parts = []
            while sum(map(len, parts)) < rng.randint(1, 100):
                digit = rng.choice("23456789")
                limit = 4 if digit in "79" else 3
                parts.append(digit * rng.randint(1, limit))
            pressed = "".join(parts)[:100]
        assert 1 <= len(pressed) <= 100000
        assert all("2" <= digit <= "9" for digit in pressed)
        cases.add(f"candidate(pressedKeys={pressed!r})")
    assert len(cases) == 599
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(pressedKeys={'2' * 100000!r})"
    if boundary not in calls:
        calls.append(boundary)
    assert 500 <= len(calls) <= 999
    return calls
