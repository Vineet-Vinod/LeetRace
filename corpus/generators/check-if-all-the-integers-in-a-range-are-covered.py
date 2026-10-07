import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Inclusive ranges and query endpoints in [1,50]."""
    rng = random.Random(seed)
    cases = set()
    if (
        "check-if-all-the-integers-in-a-range-are-covered"
        == "determine-color-of-a-chessboard-square"
    ):
        return [
            f"candidate(coordinates={chr(97 + col) + str(row)!r})"
            for col in range(8)
            for row in range(1, 9)
        ]
    if "check-if-all-the-integers-in-a-range-are-covered" == "smallest-even-multiple":
        return [f"candidate(n={value})" for value in range(1, 151)]
    while len(cases) < 600:
        left = rng.randint(1, 50)
        right = rng.randint(left, 50)
        ranges = tuple(
            sorted(
                (a, rng.randint(a, 50))
                for a in [rng.randint(1, 50) for _ in range(rng.randint(1, 8))]
            )
        )
        cases.add((ranges, left, right))
    generated_calls = [
        f"candidate(ranges={list(map(list, r))!r}, left={range_left}, right={rr})"
        for r, range_left, rr in cases
    ]
    example_calls = [
        "candidate(ranges=[[1, 2], [3, 4], [5, 6]], left=2, right=5)",
        "candidate(ranges=[[1, 10], [10, 20]], left=21, right=21)",
    ]
    generated_calls.extend(example_calls)
    unique_calls = []
    seen_calls = set()
    for generated_call in generated_calls:
        key = ast.dump(ast.parse(generated_call, mode="eval"), include_attributes=False)
        if key not in seen_calls:
            seen_calls.add(key)
            unique_calls.append(generated_call)
    return unique_calls
