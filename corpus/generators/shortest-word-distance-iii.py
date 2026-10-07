import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: list[str] = []
    seen: set[tuple[tuple[str, ...], str, str]] = set()

    def add(words: list[str], first: str, second: str) -> None:
        key = (tuple(words), first, second)
        if key not in seen:
            assert 1 <= len(words) <= 100_000
            assert all(1 <= len(word) <= 10 and word.islower() for word in words)
            assert first in words and second in words
            seen.add(key)
            cases.append(
                f"candidate(wordsDict={words!r}, word1={first!r}, word2={second!r})"
            )

    for gap in range(1, 100):
        add(["a"] + ["x"] * (gap - 1) + ["b"], "a", "b")
        add(["a"] + ["x"] * (gap - 1) + ["a"], "a", "a")
        add(["a", "b"] + ["x"] * gap + ["a", "b"], "a", "b")
    add(["a"] + ["x"] * 49_999 + ["b"] + ["x"] * 49_999, "a", "b")
    add(["a"] + ["x"] * 49_999 + ["a"] + ["x"] * 49_999, "a", "a")
    while len(cases) < 600:
        words = [rng.choice(("a", "b", "c", "d")) for _ in range(rng.randint(2, 100))]
        first, second = rng.sample(("a", "b", "c", "d"), 2)
        words[0] = first
        words[-1] = second
        add(words, first, second)
    return cases[:600]
