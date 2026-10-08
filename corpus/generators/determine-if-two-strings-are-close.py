import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[str, str]] = {
        ("abc", "bca"),
        ("a", "aa"),
        ("cabbba", "abbccc"),
        ("a" * 100_000, "a" * 100_000),
        (string.ascii_lowercase, string.ascii_lowercase[::-1]),
    }
    while len(cases) < 600:
        letters = rng.sample(string.ascii_lowercase, rng.randint(1, 8))
        counts = [rng.randint(1, 20) for _ in letters]
        word1 = "".join(letter * count for letter, count in zip(letters, counts))
        if rng.random() < 0.65:
            shuffled_counts = counts[:]
            rng.shuffle(shuffled_counts)
            word2 = "".join(
                letter * count for letter, count in zip(letters, shuffled_counts)
            )
        else:
            replacement = rng.choice(
                [char for char in string.ascii_lowercase if char not in letters]
            )
            word2 = "".join(
                letter * count
                for letter, count in zip(letters[:-1] + [replacement], counts)
            )
        cases.add((word1, word2))
    assert all(
        1 <= len(first) <= 100_000
        and 1 <= len(second) <= 100_000
        and set(first) <= set(string.ascii_lowercase)
        and set(second) <= set(string.ascii_lowercase)
        for first, second in cases
    )
    return [
        f"candidate(word1={first!r}, word2={second!r})"
        for first, second in sorted(cases)
    ]
