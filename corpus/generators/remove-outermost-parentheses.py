import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    boundary = "(" * 50000 + ")" * 50000
    calls: set[str] = {f"candidate(s={boundary!r})"}
    while len(calls) < 600:
        pieces = []
        for _ in range(rng.randint(1, 20)):
            pairs = rng.randint(1, 10)
            depth = 0
            piece = []
            for _ in range(2 * pairs):
                if depth == 0 or (depth < pairs and rng.randrange(2)):
                    piece.append("(")
                    depth += 1
                else:
                    piece.append(")")
                    depth -= 1
            piece.extend(")" for _ in range(depth))
            pieces.append("".join(piece))
        s = "".join(pieces)
        assert len(s) >= 2 and len(s) <= 100000 and s.count("(") == s.count(")")
        calls.add(f"candidate(s={s!r})")
    return sorted(calls)
