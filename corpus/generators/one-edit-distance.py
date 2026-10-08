import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    alphabet = string.ascii_letters + string.digits
    cases: set[tuple[str, str]] = {
        ("ab", "acb"),
        ("", ""),
        ("", "a"),
        ("a", "a"),
        ("a" * 10_000, "a" * 9_999 + "b"),
        ("a" * 10_000, "a" * 10_000),
    }
    while len(cases) < 600:
        size = rng.randint(0, 100)
        source = "".join(rng.choice(alphabet) for _ in range(size))
        mode = rng.randrange(3)
        if mode == 0:
            index = rng.randrange(len(source) + 1)
            target = source[:index] + rng.choice(alphabet) + source[index:]
        elif mode == 1 and source:
            index = rng.randrange(len(source))
            target = source[:index] + source[index + 1 :]
        elif source:
            index = rng.randrange(len(source))
            replacement = rng.choice(alphabet.replace(source[index], ""))
            target = source[:index] + replacement + source[index + 1 :]
        else:
            target = "a"
        cases.add((source, target))
        if rng.random() < 0.25:
            cases.add((source, source))
    assert all(
        len(source) <= 10_000
        and len(target) <= 10_000
        and set(source + target) <= set(alphabet)
        for source, target in cases
    )
    return [
        f"candidate(s={source!r}, t={target!r})" for source, target in sorted(cases)
    ]
