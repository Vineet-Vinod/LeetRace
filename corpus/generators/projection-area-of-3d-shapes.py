import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Square grids of size 1..50 with heights in [0,50]."""
    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 30)
        cases.add(tuple(tuple(rng.randint(0, 50) for _ in range(n)) for _ in range(n)))
    generated_calls = [f"candidate(grid={list(map(list, g))!r})" for g in cases]
    example_calls = [
        "candidate(grid=[[1, 2], [3, 4]])",
        "candidate(grid=[[1, 0], [0, 2]])",
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
