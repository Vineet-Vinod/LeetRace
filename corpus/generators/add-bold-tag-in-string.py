import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    alphabet = string.ascii_letters + string.digits
    calls: set[str] = set()

    def add(s: str, words: list[str]) -> None:
        assert 1 <= len(s) <= 1000 and len(words) <= 100
        assert all(1 <= len(word) <= 1000 for word in words)
        assert len(words) == len(set(words))
        assert all(set(word) <= set(alphabet) for word in [s, *words])
        calls.add(f"candidate(s={s!r}, words={words!r})")

    for s, words in [
        ("abcxyz123", ["abc", "123"]),
        ("aaabbcc", ["aaa", "aab", "bc"]),
        ("abababcd", ["ab", "aba", "abcd"]),
        ("abcdef", ["gh"]),
        ("aaa", ["a", "aa"]),
        ("aa", []),
        ("xyz", ["x", "z"]),
        ("a" * 1000, ["a", "aa", "a" * 200]),
        ("abc", ["cba"]),
        ("abc123", ["bc", "12"]),
    ]:
        add(s, words)
    add("a" * 1000, ["a" * length for length in range(1, 100)] + ["a" * 1000])
    while len(calls) < 600:
        s = "".join(rng.choice("abc123") for _ in range(rng.randint(1, 80)))
        candidates: set[str] = set()
        for _ in range(rng.randint(0, 12)):
            left = rng.randrange(len(s))
            right = rng.randint(left + 1, len(s))
            candidates.add(s[left:right])
        if rng.random() < 0.6:
            candidates.add(
                "".join(rng.choice("abc123") for _ in range(rng.randint(1, 6)))
            )
        add(s, sorted(candidates))
    return sorted(calls)
