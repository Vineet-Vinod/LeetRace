import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(0,), (1, 0), (0, 0), (1, 1, 0), (1, 0, 0)}
    if "1-bit-and-2-bit-characters" == "determine-color-of-a-chessboard-square":
        return [
            f"candidate(coordinates={chr(97 + col) + str(row)!r})"
            for col in range(8)
            for row in range(1, 9)
        ]
    if "1-bit-and-2-bit-characters" == "smallest-even-multiple":
        return [f"candidate(n={value})" for value in range(1, 151)]
    cases.add((1,) * 999 + (0,))
    while len(cases) < 600:
        length = rng.randint(1, 1000)
        bits = tuple(rng.randrange(2) for _ in range(length - 1)) + (0,)
        cases.add(bits)
    calls = [f"candidate(bits={list(bits)!r})" for bits in cases]
    calls.extend(["candidate(bits=[1, 1, 1, 0])"])
    return list(dict.fromkeys(calls))
