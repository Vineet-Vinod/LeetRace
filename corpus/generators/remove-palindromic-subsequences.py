import random


def palindrome(rng: random.Random, length: int) -> str:
    half_length = length // 2
    half = "".join(rng.choice("ab") for _ in range(half_length))
    center = rng.choice("ab") if length % 2 else ""
    return half + center + half[::-1]


def non_palindrome(rng: random.Random, length: int) -> str:
    if length == 1:
        return rng.choice("ab")
    middle = "".join(rng.choice("ab") for _ in range(length - 2))
    return "a" + middle + "b"


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        "ababa",
        "abb",
        "baabb",
        "a",
        "ab" * 500,
        "a" * 1000,
        "b" + "a" * 998 + "a",
    }
    while len(cases) < 600:
        length = rng.randint(1, 1000)
        cases.add(palindrome(rng, length))
        length = rng.randint(1, 1000)
        cases.add(non_palindrome(rng, length))
    return [f"candidate(s={value!r})" for value in cases]
