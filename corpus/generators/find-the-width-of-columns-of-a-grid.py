import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Nonempty rectangular integer matrices with dimensions at most 100."""
    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        rows = rng.randint(1, 20)
        cols = rng.randint(1, 15)
        grid = tuple(
            tuple(rng.randint(-(10**9), 10**9) for _ in range(cols))
            for _ in range(rows)
        )
        cases.add(grid)
    generated_calls = [f"candidate(grid={list(map(list, g))!r})" for g in cases]
    example_calls = [
        "candidate(grid=[[1], [22], [333]])",
        "candidate(grid=[[-15, 1, 3], [15, 7, 12], [5, 6, -2]])",
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
