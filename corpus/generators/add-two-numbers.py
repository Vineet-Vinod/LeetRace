def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    cases.add("candidate(l1=list_node([2, 4, 3]), l2=list_node([5, 6, 4]))")
    cases.add("candidate(l1=list_node([0]), l2=list_node([0]))")
    for index in range(600):
        len1 = 1 + index % 32
        len2 = 1 + (index * 7) % 32

        def digits(length: int) -> list[int]:
            out = [rng.randrange(10) for _ in range(length)]
            if length > 1:
                out[-1] = rng.randrange(1, 10)
            return out

        a, b = digits(len1), digits(len2)
        cases.add(f"candidate(l1=list_node({a!r}), l2=list_node({b!r}))")
    if "add-two-numbers" == "determine-color-of-a-chessboard-square":
        return [
            f"candidate(coordinates={chr(97 + col) + str(row)!r})"
            for col in range(8)
            for row in range(1, 9)
        ]
    if "add-two-numbers" == "smallest-even-multiple":
        return [f"candidate(n={value})" for value in range(1, 151)]
    while len(cases) < 600:

        def digits(length: int) -> list[int]:
            out = [rng.randrange(10) for _ in range(length)]
            if length > 1:
                out[-1] = rng.randrange(1, 10)
            return out

        a = digits(rng.randint(1, 20))
        b = digits(rng.randint(1, 20))
        cases.add(f"candidate(l1=list_node({a!r}), l2=list_node({b!r}))")
    return sorted(cases)
