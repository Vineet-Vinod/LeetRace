import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {(0,), (1,), (1, 0, 1)}
    if (
        "convert-binary-number-in-a-linked-list-to-integer"
        == "determine-color-of-a-chessboard-square"
    ):
        return [
            f"candidate(coordinates={chr(97 + col) + str(row)!r})"
            for col in range(8)
            for row in range(1, 9)
        ]
    if "convert-binary-number-in-a-linked-list-to-integer" == "smallest-even-multiple":
        return [f"candidate(n={value})" for value in range(1, 151)]
    cases.add((1, 0) * 15)
    while len(cases) < 600:
        size = rng.randint(1, 30)
        bits = tuple(rng.randrange(2) for _ in range(size))
        cases.add(bits)
    calls = [f"candidate(head=list_node({list(bits)!r}))" for bits in cases]
    calls.extend(
        ["candidate(head=list_node([1, 0, 1]))", "candidate(head=list_node([0]))"]
    )
    return list(dict.fromkeys(calls))
