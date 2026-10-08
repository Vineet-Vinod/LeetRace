import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[str, ...]] = {
        ("aa", "ab", "bc"),
        ("ab", "b"),
        ("aaa", "c", "aba"),
        ("a",),
        ("ab", "ba"),
    }
    cases.add(tuple("a" for _ in range(1000)))
    cases.add(("a" * 50,) + tuple("a" for _ in range(950)))
    alphabet = string.ascii_lowercase[:6]
    while len(cases) < 600:
        count = rng.randint(1, 10)
        words = tuple(
            "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 8)))
            for _ in range(count)
        )
        cases.add(words)
    assert all(
        1 <= len(words) <= 1000
        and 1 <= sum(map(len, words)) <= 1000
        and all(
            1 <= len(word) <= 50 and set(word) <= set(string.ascii_lowercase)
            for word in words
        )
        for words in cases
    )
    return [f"candidate(words={list(words)!r})" for words in sorted(cases)]
