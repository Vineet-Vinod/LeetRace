import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    alphabet = string.ascii_lowercase
    while len(calls) < 600:
        group_count = 1 + rng.randrange(8)
        letters = rng.sample(alphabet, group_count)
        target_counts = [1 + rng.randrange(8) for _ in letters]
        s = "".join(letter * count for letter, count in zip(letters, target_counts))
        valid_count = rng.randrange(7)
        words = []
        for _ in range(valid_count):
            counts = [
                rng.randint(1, count) if count >= 3 else count
                for count in target_counts
            ]
            words.append(
                "".join(letter * count for letter, count in zip(letters, counts))
            )
        for _ in range(8 - valid_count):
            index = rng.randrange(group_count)
            counts = target_counts[:]
            counts[index] += 1
            words.append(
                "".join(letter * count for letter, count in zip(letters, counts))
            )
        assert 1 <= len(s) <= 100 and 1 <= len(words) <= 100
        assert all(1 <= len(word) <= 100 for word in words)
        calls.add(f"candidate(s={s!r}, words={words!r})")
    calls.add("candidate(s='a' * 100, words=['a', 'a' * 100, 'b'])")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(s='heeellooo', words=['hello', 'hi', 'helo'])",
    "candidate(s='zzzzzyyyyy', words=['zzyy', 'zy', 'zyy'])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
