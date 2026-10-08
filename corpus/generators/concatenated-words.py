import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(words: list[str]) -> None:
        assert 1 <= len(words) <= 10000 and len(set(words)) == len(words)
        assert 1 <= sum(map(len, words)) <= 100000
        assert all(
            1 <= len(w) <= 30 and w.isascii() and w.islower() and w.isalpha()
            for w in words
        )
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in [("words", words)])
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(
        words=[
            "cat",
            "cats",
            "catsdogcats",
            "dog",
            "dogcatsdog",
            "hippopotamuses",
            "rat",
            "ratcatdogcat",
        ]
    )
    add(words=["a" * i for i in range(1, 31)])
    add(
        words=[
            "".join(chr(97 + (i // 26**j) % 26) for j in range(10))
            for i in range(10000)
        ]
    )
    add(
        words=[
            "cat",
            "cats",
            "catsdogcats",
            "dog",
            "dogcatsdog",
            "hippopotamuses",
            "rat",
            "ratcatdogcat",
        ]
    )
    add(words=["cat", "dog", "catdog"])
    while len(calls) < 600:
        base = {
            "".join(rng.choices("abcde", k=rng.randint(1, 6)))
            for _ in range(rng.randint(3, 15))
        }
        words = set(base)
        if len(calls) % 3 != 0:
            for _ in range(12):
                words.add("".join(rng.choices(sorted(base), k=rng.randint(2, 4))))
        add(words=rng.sample(sorted(words), len(words)))
    return calls
