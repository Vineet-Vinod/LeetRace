import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[str, ...]] = {
        ("abba", "baba", "bbaa", "cd", "cd"),
        ("a", "b", "c"),
    }
    cases.add(("abcdefghij",) * 100)
    while len(cases) < 600:
        words = tuple(
            "".join(
                rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, 10))
            )
            for _ in range(rng.randint(1, 100))
        )
        cases.add(words)
    calls = [f"candidate(words={list(words)!r})" for words in cases]
    calls.extend(["candidate(words=['a', 'b', 'c', 'd', 'e'])"])
    return list(dict.fromkeys(calls))
