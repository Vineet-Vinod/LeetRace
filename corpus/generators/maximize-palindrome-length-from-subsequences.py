import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(word1: str, word2: str) -> None:
        assert (
            1 <= len(word1) <= 1000
            and 1 <= len(word2) <= 1000
            and all("a" <= c <= "z" for c in word1 + word2)
        )
        call = (
            "candidate("
            + ", ".join(
                f"{key}={value!r}"
                for key, value in [("word1", word1), ("word2", word2)]
            )
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(word1="cacb", word2="cbba")
    add(word1="a" * 1000, word2="a" * 1000)
    add(word1="ab" * 500, word2="ba" * 500)
    add(word1="a" * 1000, word2="b" * 1000)
    add(word1="cacb", word2="cbba")
    add(word1="ab", word2="ab")
    add(word1="aa", word2="bb")
    while len(calls) < 600:
        alphabet = "abcde"
        word1 = "".join(rng.choices(alphabet, k=rng.randint(1, 35)))
        word2 = "".join(
            rng.choices(alphabet if len(calls) % 4 else "fgh", k=rng.randint(1, 35))
        )
        add(word1=word1, word2=word2)
    return calls
