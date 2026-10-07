import random
import string


def _prefix(words: list[str]) -> str:
    length = min(map(len, words))
    index = 0
    while index < length and all(word[index] == words[0][index] for word in words):
        index += 1
    return words[0][:index]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    nonempty: set[str] = set()
    empty: set[str] = set()
    alphabet = string.ascii_lowercase

    while len(nonempty) < 300:
        prefix = "".join(rng.choices(alphabet, k=rng.randint(1, 100)))
        words = [prefix]
        words.extend(
            prefix + "".join(rng.choices(alphabet, k=rng.randint(0, 200 - len(prefix))))
            for _ in range(rng.randint(1, 20))
        )
        assert _prefix(words) == prefix
        nonempty.add(f"candidate(strs={words!r})")

    while len(empty) < 300:
        first = rng.choice(alphabet)
        second = rng.choice(alphabet.replace(first, ""))
        words = [
            first + "".join(rng.choices(alphabet, k=rng.randint(0, 20)))
            for _ in range(rng.randint(1, 20))
        ]
        words.append(second + "".join(rng.choices(alphabet, k=rng.randint(0, 20))))
        assert _prefix(words) == ""
        empty.add(f"candidate(strs={words!r})")

    return sorted(nonempty | empty)
