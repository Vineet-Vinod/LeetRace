import random
import string


_ALLOWED = string.ascii_letters + string.digits + "!@#$%^&*()_+-=',.: "


def generate(seed: int = 0) -> list[str]:
    """Generate empty, boundary, whitespace, letter, digit, and punctuation inputs."""
    rng = random.Random(seed)
    cases = {
        "",
        "Hello, my name is John",
        "Hello",
        "   ",
        "a  b",
        "1234567890",
        "!@#$%^&*()_+-=',.:",
        "Letters123! punctuation?".replace("?", "."),
        "a b c d e",
        "A1! b2@ C3#",
        "a" * 300,
        ("A1! b2@ C3# " * 25),
    }
    while len(cases) < 600:
        length = rng.randint(0, 300)
        cases.add("".join(rng.choice(_ALLOWED) for _ in range(length)))

    assert len(cases) == 600
    assert all(len(value) <= 300 and set(value) <= set(_ALLOWED) for value in cases)
    assert "" in cases and max(map(len, cases)) == 300
    assert any(any(char.isdigit() for char in value) for value in cases)
    assert any(any(char in "!@#$%^&*()_+-=',.:" for char in value) for value in cases)
    return [f"candidate(s={value!r})" for value in sorted(cases)]
