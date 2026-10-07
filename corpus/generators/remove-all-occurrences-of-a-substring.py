import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[str, str]] = {
        ("daabcbaabcbc", "abc"),
        ("axxxxyyyyb", "xy"),
        ("aaaaa", "aa"),
        ("abc", "d"),
        ("a", "a"),
        ("a" * 1000, "a" * 1000),
    }
    alphabet = string.ascii_lowercase[:6]
    while len(cases) < 600:
        s = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 100)))
        part = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 20)))
        cases.add((s, part))
    assert all(
        1 <= len(s) <= 1000
        and 1 <= len(part) <= 1000
        and set(s) <= set(string.ascii_lowercase)
        and set(part) <= set(string.ascii_lowercase)
        for s, part in cases
    )
    return [f"candidate(s={s!r}, part={part!r})" for s, part in sorted(cases)]
