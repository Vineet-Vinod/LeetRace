import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[str, str]] = {("abcdefd", "d"), ("xyxzxe", "z"), ("abcd", "z")}
    cases.add(("a" * 249 + "z", "z"))
    while len(cases) < 600:
        word = "".join(
            rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, 250))
        )
        cases.add((word, rng.choice(string.ascii_lowercase)))
    return [f"candidate(word={word!r}, ch={ch!r})" for word, ch in cases]
