import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Coordinates in [1,10000], point count 1..10000."""
    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        x, y = rng.randint(1, 100), rng.randint(1, 100)
        points = tuple(
            (rng.randint(1, 100), rng.randint(1, 100))
            for _ in range(rng.randint(1, 25))
        )
        cases.add((x, y, points))
    generated_calls = [
        f"candidate(x={x}, y={y}, points={list(map(list, p))!r})" for x, y, p in cases
    ]
    example_calls = [
        "candidate(x=3, y=4, points=[[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]])",
        "candidate(x=3, y=4, points=[[3, 4]])",
        "candidate(x=3, y=4, points=[[2, 3]])",
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
