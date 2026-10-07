import random


def generate(seed: int = 0) -> list[str]:
    """Use carry-free repeated-digit positives and varied valid negative triples."""
    rng = random.Random(seed)
    positives = {("acb", "cba", "cdb"), ("aaa", "a", "aaaa")}
    while len(positives) < 300:
        length = rng.randint(1, 8)
        first_digit = rng.randrange(10)
        second_digit = rng.randrange(10 - first_digit)
        target_digit = first_digit + second_digit
        positives.add(
            (
                chr(97 + first_digit) * length,
                chr(97 + second_digit) * length,
                chr(97 + target_digit) * length,
            )
        )

    negatives = {("a", "a", "b"), ("aaa", "a", "aab")}
    while len(negatives) < 300:
        words = tuple(
            "".join(rng.choice("abcdefghij") for _ in range(rng.randint(1, 8)))
            for _ in range(3)
        )
        first, second, target = words
        first_value = int("".join(str(ord(char) - 97) for char in first))
        second_value = int("".join(str(ord(char) - 97) for char in second))
        target_value = int("".join(str(ord(char) - 97) for char in target))
        if first_value + second_value != target_value:
            negatives.add(words)

    cases = sorted(positives) + sorted(negatives)

    def numeric_value(word: str) -> int:
        digits = "".join(str(ord(char) - 97) for char in word)
        return int(digits)

    assert len(cases) == len(set(cases)) == 600
    assert all(
        1 <= len(word) <= 8 and set(word) <= set("abcdefghij")
        for case in cases
        for word in case
    )
    assert all(
        numeric_value(a) + numeric_value(b) == numeric_value(target)
        for a, b, target in positives
    )
    assert all(
        numeric_value(a) + numeric_value(b) != numeric_value(target)
        for a, b, target in negatives
    )
    return [
        f"candidate(firstWord={first!r}, secondWord={second!r}, targetWord={target!r})"
        for first, second, target in cases
    ]
