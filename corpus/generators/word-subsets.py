import random


def generate(seed: int = 0) -> list[str]:
    r = random.Random(seed)
    cases = []
    seen = set()

    def add(words1, words2):
        key = (tuple(words1), tuple(words2))
        if key not in seen:
            assert 1 <= len(words1) <= 10_000 and 1 <= len(words2) <= 10_000
            assert all(1 <= len(w) <= 10 and w.islower() for w in words1 + words2)
            assert len(set(words1)) == len(words1)
            seen.add(key)
            cases.append(f"candidate(words1={words1!r}, words2={words2!r})")

    for i in range(300):
        req = "abc"[i % 3]
        words1 = []
        while len(words1) < 10:
            word = req + "".join(r.choice("defgh") for _ in range(r.randint(0, 5)))
            if word not in words1:
                words1.append(word)
        words2 = [req]
        add(words1, words2)
    for _ in range(300):
        words1 = []
        while len(words1) < 10:
            w = "".join(
                r.choice("abcdefghijklmnopqrstuvwxy") for _ in range(r.randint(1, 8))
            )
            if w not in words1:
                words1.append(w)
        add(words1, ["z"])
    add(
        [
            "a"
            + chr(97 + (i // 676) % 26)
            + chr(97 + (i // 26) % 26)
            + chr(97 + i % 26)
            for i in range(10_000)
        ],
        ["a"],
    )
    add(
        [
            "a" + "".join(chr(98 + (j // (24**power)) % 24) for power in (2, 1, 0))
            for j in range(1000)
        ],
        ["z"],
    )
    return cases
