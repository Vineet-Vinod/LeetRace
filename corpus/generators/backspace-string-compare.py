import random
import string


def encode(text: str, rng: random.Random) -> str:
    pieces: list[str] = []
    for char in text:
        pieces.append(char)
        noise = "".join(rng.choice(string.ascii_lowercase) for _ in range(2))
        pieces.append(noise + "##")
    return "".join(pieces) or "#"


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[str, str]] = {
        ("ab#c", "ad#c"),
        ("ab##", "c#d#"),
        ("a#c", "b"),
        ("#", "#"),
        ("a", "b"),
        ("a" * 100 + "#" * 100, "#" * 200),
        ("a" * 200, "b" * 200),
    }
    while len(cases) < 600:
        text = "".join(
            rng.choice(string.ascii_lowercase) for _ in range(rng.randint(0, 30))
        )
        if rng.randrange(2):
            left = encode(text, rng)
            right = encode(text, rng)
        else:
            other = rng.choice(string.ascii_lowercase)
            if text.endswith(other):
                other = "a" if other != "a" else "b"
            left = encode(text, rng)
            right = encode(text + other, rng)
        cases.add((left, right))
    return [f"candidate(s={left!r}, t={right!r})" for left, right in cases]
