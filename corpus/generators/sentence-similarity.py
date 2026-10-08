import random
import string


def word(rng: random.Random) -> str:
    return "".join(rng.choice(string.ascii_letters) for _ in range(rng.randint(1, 20)))


def similar_case(
    rng: random.Random, size: int
) -> tuple[tuple[str, ...], tuple[str, ...], tuple[tuple[str, str], ...]]:
    first = tuple(word(rng) for _ in range(size))
    second: list[str] = []
    pairs: set[tuple[str, str]] = set()
    for value in first:
        related = word(rng)
        second.append(related)
        if related != value:
            pairs.add(tuple(sorted((value, related))))
    return first, tuple(second), tuple(sorted(pairs))


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[str, ...], tuple[str, ...], tuple[tuple[str, str], ...]]] = {
        (
            ("great", "acting", "skills"),
            ("fine", "drama", "talent"),
            (("great", "fine"), ("acting", "drama"), ("skills", "talent")),
        ),
        (("great",), ("great",), ()),
        (("great",), ("doubleplus", "good"), (("doubleplus", "great"),)),
        (("A" * 20,) * 1000, ("A" * 20,) * 1000, ()),
        (
            tuple("left" + str(index) for index in range(1000)),
            tuple("right" + str(index) for index in range(1000)),
            tuple(("left" + str(index), "right" + str(index)) for index in range(1000)),
        ),
    }
    while len(cases) < 600:
        if rng.randrange(2):
            cases.add(similar_case(rng, rng.randint(1, 100)))
        else:
            first_size = rng.randint(1, 100)
            second_size = first_size if rng.randrange(4) else rng.randint(1, 100)
            first = tuple(word(rng) for _ in range(first_size))
            second = tuple(word(rng) for _ in range(second_size))
            pairs = {
                tuple(sorted((word(rng), word(rng))))
                for _ in range(rng.randint(0, 100))
            }
            cases.add((first, second, tuple(sorted(pairs))))
    calls = [
        f"candidate(sentence1={list(first)!r}, sentence2={list(second)!r}, similarPairs={[list(pair) for pair in pairs]!r})"
        for first, second, pairs in cases
    ]
    calls.extend(
        [
            "candidate(sentence1=['great', 'acting', 'skills'], sentence2=['fine', 'drama', 'talent'], similarPairs=[['great', 'fine'], ['drama', 'acting'], ['skills', 'talent']])",
            "candidate(sentence1=['great'], sentence2=['doubleplus', 'good'], similarPairs=[['great', 'doubleplus']])",
        ]
    )
    return list(dict.fromkeys(calls))
