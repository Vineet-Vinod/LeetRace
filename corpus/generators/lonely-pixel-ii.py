def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases: set[str] = set()

    def add(picture: list[list[str]], target: int) -> None:
        rows, cols = len(picture), len(picture[0])
        assert 1 <= rows <= 200 and 1 <= cols <= 200
        assert all(len(row) == cols for row in picture)
        assert all(pixel in ("B", "W") for row in picture for pixel in row)
        assert 1 <= target <= min(rows, cols)
        cases.add(f"candidate(picture={picture!r}, target={target})")

    add(
        [
            ["W", "B", "W", "B", "B", "W"],
            ["W", "B", "W", "B", "B", "W"],
            ["W", "B", "W", "B", "B", "W"],
            ["W", "W", "B", "W", "B", "W"],
        ],
        3,
    )
    add([["B"] * 200 for _ in range(200)], 200)

    # Identical rows with exactly m black pixels guarantee m^2 qualifying cells
    # when target equals the row count m.
    for index in range(300):
        rows = 1 + index % 30
        cols = max(rows, 1 + (index * 37) % 200)
        black_cols = set(rng.sample(range(cols), rows))
        pattern = ["B" if col in black_cols else "W" for col in range(cols)]
        add([pattern.copy() for _ in range(rows)], rows)

    # Repeating one black pixel across multiple rows guarantees zero when target=1.
    for index in range(300):
        rows = 2 + index % 29
        cols = max(rows, 1 + (index * 31) % 200)
        black_col = index % cols
        pattern = ["B" if col == black_col else "W" for col in range(cols)]
        add([pattern.copy() for _ in range(rows)], 1)

    while len(cases) < 600:
        rows = rng.randint(1, 200)
        cols = rng.randint(1, 200)
        picture = [[rng.choice(("B", "W")) for _ in range(cols)] for _ in range(rows)]
        add(picture, rng.randint(1, min(rows, cols)))

    result = list(cases)
    rng.shuffle(result)
    return result
