import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(words, letters, score):
        assert 1 <= len(words) <= 14 and all(1 <= len(w) <= 15 for w in words)
        assert 1 <= len(letters) <= 100 and all(len(c) == 1 for c in letters)
        assert len(score) == 26 and all(0 <= v <= 10 for v in score)
        assert all("a" <= c <= "z" for w in words + letters for c in w)
        call = (
            "candidate("
            + ", ".join(
                f"{name}={value!r}"
                for name, value in (
                    ("words", words),
                    ("letters", letters),
                    ("score", score),
                )
            )
            + ")"
        )
        calls[call] = None

    add(
        words=["dog", "cat", "dad", "good"],
        letters=["a", "a", "c", "d", "d", "d", "g", "o", "o"],
        score=[
            1,
            0,
            9,
            5,
            0,
            0,
            3,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            2,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
    )
    add(
        words=["xxxz", "ax", "bx", "cx"],
        letters=["z", "a", "b", "c", "x", "x", "x"],
        score=[
            4,
            4,
            4,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            5,
            0,
            10,
        ],
    )
    add(
        words=["leetcode"],
        letters=["l", "e", "t", "c", "o", "d"],
        score=[
            0,
            0,
            1,
            1,
            1,
            0,
            0,
            0,
            0,
            0,
            0,
            1,
            0,
            0,
            1,
            0,
            0,
            0,
            0,
            1,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
    )
    add(words=["a" * 15] * 14, letters=["a"] * 100, score=[10] * 26)
    add(words=["z"] * 14, letters=["z"] * 14, score=[10] * 26)
    while len(calls) < 600:
        words = [
            "".join(rng.choices("abcdef", k=rng.randint(1, 8)))
            for _ in range(rng.randint(1, 9))
        ]
        mode = rng.randrange(4)
        if mode == 0:
            letters = list("".join(words))
        elif mode == 1:
            letters = ["z"] * rng.randint(1, 30)
        else:
            letters = rng.choices("abcdef", k=rng.randint(1, 40))
        score = [rng.randint(0, 10) for _ in range(26)]
        if mode == 3:
            score = [0] * 26
        add(words=words, letters=letters, score=score)
    return list(calls)
