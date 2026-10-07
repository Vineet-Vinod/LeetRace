from __future__ import annotations
import random

EXAMPLE_CALLS = [
    "candidate(word1=['ab', 'c'], word2=['a', 'bc'])",
    "candidate(word1=['a', 'cb'], word2=['ab', 'c'])",
    "candidate(word1=['abc', 'd', 'defg'], word2=['abcddefg'])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    equal = {
        EXAMPLE_CALLS[0],
        EXAMPLE_CALLS[2],
        "candidate(word1=['a'*1000], word2=['a'*500, 'a'*500])",
    }
    different = {EXAMPLE_CALLS[1]}

    def split(text: str) -> list[str]:
        pieces = []
        index = 0
        while index < len(text):
            width = rng.randint(1, min(25, len(text) - index))
            pieces.append(text[index : index + width])
            index += width
        return pieces

    while len(equal) < 300:
        text = "".join(
            rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(rng.randint(1, 500))
        )
        equal.add(f"candidate(word1={split(text)!r}, word2={split(text)!r})")
    while len(different) < 300:
        first = "".join(
            rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(rng.randint(1, 500))
        )
        replacement = "a" if first[-1] != "a" else "b"
        second = first[:-1] + replacement
        different.add(f"candidate(word1={split(first)!r}, word2={split(second)!r})")
    assert len(equal) == 300 and len(different) == 300
    return sorted(equal | different)
