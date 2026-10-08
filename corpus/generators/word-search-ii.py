import random
from itertools import product


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        validate(kwargs)
        call = (
            "candidate(" + ", ".join(k + "=" + repr(v) for k, v in kwargs.items()) + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    def letters(text):
        return all("a" <= ch <= "z" for ch in text)

    def array(values, minimum, maximum, length):
        assert 1 <= len(values) <= length
        assert all(minimum <= v <= maximum for v in values)

    def validate(d):
        board, words = d["board"], d["words"]
        assert 1 <= len(board) <= 12 and 1 <= len(board[0]) <= 12
        assert all(
            len(row) == len(board[0])
            and all(len(ch) == 1 and letters(ch) for ch in row)
            for row in board
        )
        assert 1 <= len(words) <= 30000 and len(set(words)) == len(words)
        assert all(1 <= len(w) <= 10 and letters(w) for w in words)

    add(
        board=[
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ],
        words=["oath", "pea", "eat", "rain"],
    )
    add(board=[["a", "b"], ["c", "d"]], words=["abcb"])
    add(board=[["a"] * 12 for _ in range(12)], words=["a" * i for i in range(1, 11)])
    add(
        board=[["z"]],
        words=["".join(p) for p in product("abcdefghijklmn", repeat=4)][:30000] + [],
    )
    while len(calls) < 600:
        m, n = rng.randint(1, 6), rng.randint(1, 6)
        board = [[rng.choice("abcde") for _ in range(n)] for _ in range(m)]
        words = {
            "".join(rng.choice("abcdef") for _ in range(rng.randint(1, 10)))
            for _ in range(rng.randint(1, 30))
        }
        # Include words from real simple paths in a substantial positive family.
        for _ in range(rng.randint(1, 10)):
            r, c = rng.randrange(m), rng.randrange(n)
            visited = {(r, c)}
            word = board[r][c]
            for _ in range(rng.randint(0, 9)):
                options = [
                    (a, b)
                    for a, b in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1))
                    if 0 <= a < m and 0 <= b < n and (a, b) not in visited
                ]
                if not options:
                    break
                r, c = rng.choice(options)
                visited.add((r, c))
                word += board[r][c]
            words.add(word)
        if rng.randrange(4) == 0:
            words = {
                "z" + "".join(rng.choice("abcde") for _ in range(rng.randint(0, 9)))
                for _ in range(20)
            }
        add(board=board, words=sorted(words))
    assert len(calls) == 600
    return calls
