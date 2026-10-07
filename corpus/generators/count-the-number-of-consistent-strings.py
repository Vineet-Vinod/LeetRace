import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[str, tuple[str, ...]]] = {
        ("ab", ("ad", "bd", "aaab", "baa", "badab")),
        ("abc", ("a", "b", "c")),
    }
    cases.add((string.ascii_lowercase, ("a" * 10,) * 10_000))
    while len(cases) < 600:
        allowed = "".join(rng.sample(string.ascii_lowercase, rng.randint(1, 26)))
        words = tuple(
            "".join(
                rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, 10))
            )
            for _ in range(rng.randint(1, 1000))
        )
        cases.add((allowed, words))
    calls = [
        f"candidate(allowed={allowed!r}, words={list(words)!r})"
        for allowed, words in cases
    ]
    calls.extend(
        [
            "candidate(allowed='abc', words=['a', 'b', 'c', 'ab', 'ac', 'bc', 'abc'])",
            "candidate(allowed='cad', words=['cc', 'acd', 'b', 'ba', 'bac', 'bad', 'ac', 'd'])",
        ]
    )
    return list(dict.fromkeys(calls))
