import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[str, str, tuple[int, ...]]] = {
        ("abcacb", "ab", (3, 1, 0)),
        ("abcbddddd", "abcd", (3, 2, 1, 4, 5, 6)),
        ("abcab", "abc", (0, 1, 2, 3)),
        ("a" * 100_000, "a" * 100_000, tuple(range(99_999))),
        ("a" * 100_000, "a", tuple(range(99_999))),
    }
    alphabet = string.ascii_lowercase[:5]
    while len(cases) < 600:
        size = rng.randint(2, 80)
        s = "".join(rng.choice(alphabet) for _ in range(size))
        positions = sorted(rng.sample(range(size), rng.randint(1, size)))
        p = "".join(s[index] for index in positions)
        removable = tuple(rng.sample(range(size), rng.randint(0, size - 1)))
        cases.add((s, p, removable))
    assert all(
        1 <= len(p) <= len(s) <= 100_000
        and len(removable) < len(s)
        and len(set(removable)) == len(removable)
        and all(0 <= index < len(s) for index in removable)
        and iter_subsequence(s, p)
        for s, p, removable in cases
    )
    return [
        f"candidate(s={s!r}, p={p!r}, removable={list(removable)!r})"
        for s, p, removable in sorted(cases)
    ]


def iter_subsequence(s: str, p: str) -> bool:
    position = 0
    for char in s:
        if position < len(p) and char == p[position]:
            position += 1
    return position == len(p)
