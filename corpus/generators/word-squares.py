import random
import itertools


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def valid(words):
        return (
            1 <= len(words) <= 1000
            and len(set(words)) == len(words)
            and 1 <= len(words[0]) <= 4
            and all(
                len(w) == len(words[0]) and all("a" <= c <= "z" for c in w)
                for w in words
            )
        )

    def emit(**args):
        assert valid(**args), args
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in args.items()) + ")"
        calls[call] = None

    emit(words=["area", "lead", "wall", "lady", "ball"])
    emit(words=["abat", "baba", "atan", "atal"])
    emit(words=list("abcdefghijklmnopqrstuvwxyz"))
    emit(words=["".join(p) for p in itertools.product("ab", repeat=4)])
    # 1000 distinct length-four words sharing a first letter absent from all second letters:
    # no second row can match the required prefix, so the maximum input has bounded output.
    emit(
        words=[
            "a" + "".join(p)
            for p in itertools.islice(
                itertools.product("bcdefghijklmnopqrstuvwxyz", repeat=3), 1000
            )
        ]
    )
    while len(calls) < 600:
        width = rng.randint(1, 4)
        alphabet = rng.choice(["abc", "abcd", "abcdefghijklmnopqrstuvwxyz"])
        count = rng.randint(1, min(20, len(alphabet) ** width))
        words = []
        while len(words) < count:
            word = "".join(rng.choice(alphabet) for _ in range(width))
            if word not in words:
                words.append(word)
        # Half the families contain a constructed symmetric matrix, guaranteeing a square.
        if rng.randrange(2):
            matrix = [[""] * width for _ in range(width)]
            for i in range(width):
                for j in range(i, width):
                    matrix[i][j] = matrix[j][i] = rng.choice(alphabet)
            words = list(dict.fromkeys(words + ["".join(row) for row in matrix]))
        emit(words=words)
    assert len(calls) == 600
    return list(calls)
