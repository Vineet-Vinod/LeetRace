import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], tuple[tuple[int, ...], ...]]] = {
        ((15, 88), ((88,), (15,))),
        ((49, 18, 16), ((16, 18, 49),)),
        (tuple(range(1, 101)), tuple((value,) for value in range(100, 0, -1))),
    }
    while len(cases) < 600:
        size = rng.randint(2, 100)
        arr = rng.sample(range(1, 101), size)
        can_form = rng.choice((True, False))
        pieces: list[tuple[int, ...]] = []
        index = 0
        while index < size:
            width = rng.randint(1, min(8, size - index))
            if not can_form and not pieces and width == 1:
                width = 2
            piece = tuple(arr[index : index + width])
            if not can_form and not pieces:
                piece = piece[::-1]
            pieces.append(piece)
            index += width
        rng.shuffle(pieces)
        cases.add((tuple(arr), tuple(pieces)))
    calls = [
        f"candidate(arr={list(arr)!r}, pieces={[list(piece) for piece in pieces]!r})"
        for arr, pieces in cases
    ]
    calls.extend(["candidate(arr=[91, 4, 64, 78], pieces=[[78], [4, 64], [91]])"])
    return list(dict.fromkeys(calls))
