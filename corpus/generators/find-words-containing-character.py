import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[str, ...], str]] = {(("leet", "code"), "e"), (("abc",), "z")}
    cases.add((("a" * 50,) * 49 + ("z" * 50,), "a"))
    while len(cases) < 600:
        words = tuple(
            "".join(
                rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, 50))
            )
            for _ in range(rng.randint(1, 50))
        )
        cases.add((words, rng.choice(string.ascii_lowercase)))
    calls = [f"candidate(words={list(words)!r}, x={x!r})" for words, x in cases]
    calls.extend(
        [
            "candidate(words=['abc', 'bcd', 'aaaa', 'cbc'], x='a')",
            "candidate(words=['abc', 'bcd', 'aaaa', 'cbc'], x='z')",
        ]
    )
    return list(dict.fromkeys(calls))
