import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        words = [
            "".join(
                rng.choice(string.ascii_lowercase[:8])
                for _ in range(rng.randint(1, 12))
            )
            for _ in range(rng.randint(1, 40))
        ]
        dictionary = sorted(set(words))
        sentence_words = [
            "".join(
                rng.choice(string.ascii_lowercase[:8])
                for _ in range(rng.randint(1, 30))
            )
            for _ in range(rng.randint(1, 40))
        ]
        sentence = " ".join(sentence_words)
        calls.add(f"candidate(dictionary={dictionary!r}, sentence={sentence!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(dictionary=['a', 'b', 'c'], sentence='aadsfasf absbs bbab cadsfafs')",
    "candidate(dictionary=['cat', 'bat', 'rat'], sentence='the cattle was rattled by the battery')",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
