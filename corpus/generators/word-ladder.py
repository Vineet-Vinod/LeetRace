import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def valid(d):
        a = d["beginWord"]
        b = d["endWord"]
        words = d["wordList"]
        assert (
            1 <= len(a) <= 10
            and len(b) == len(a)
            and a != b
            and 1 <= len(words) <= 5000
            and len(set(words)) == len(words)
        )
        assert all(
            len(w) == len(a) and all("a" <= c <= "z" for c in w) for w in words + [a, b]
        )

    def add(**kwargs):
        valid(kwargs)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(
        beginWord="hit",
        endWord="cog",
        wordList=["hot", "dot", "dog", "lot", "log", "cog"],
    )
    add(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log"])

    def word(i):
        chars = []
        for _ in range(10):
            chars.append(chr(97 + i % 26))
            i //= 26
        return "".join(reversed(chars))

    add(beginWord="a" * 10, endWord="z" * 10, wordList=[word(i) for i in range(5000)])
    t = 0
    while len(calls) < 600:
        length = rng.randint(1, 6)
        begin = "".join(rng.choice("abcd") for _ in range(length))
        end = begin
        while end == begin:
            end = "".join(rng.choice("abcd") for _ in range(length))
        words = set()
        capacity = 4**length
        for _ in range(rng.randint(1, min(50, capacity))):
            words.add("".join(rng.choice("abcd") for _ in range(length)))
        if t % 3 == 0:
            current = list(begin)
            for i, c in enumerate(end):
                current[i] = c
                words.add("".join(current))
        if t % 3 == 1:
            words.discard(end)
        if not words:
            words.add(begin)
        add(beginWord=begin, endWord=end, wordList=sorted(words))
        t += 1
    return calls
