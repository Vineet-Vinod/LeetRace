import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        "abacaba",
        "ssssss",
        "a",
        string.ascii_lowercase * (100_000 // 26)
        + string.ascii_lowercase[: 100_000 % 26],
    }
    while len(cases) < 600:
        cases.add(
            "".join(
                rng.choice(string.ascii_lowercase[:12])
                for _ in range(rng.randint(1, 100))
            )
        )
    assert all(
        1 <= len(s) <= 100_000 and set(s) <= set(string.ascii_lowercase) for s in cases
    )
    return [f"candidate(s={s!r})" for s in sorted(cases)]
