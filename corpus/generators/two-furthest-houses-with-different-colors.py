import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Arrays of length at least 2 with colors in [1,4]."""
    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        colors = list(rng.randint(0, 100) for _ in range(rng.randint(2, 100)))
        if all(color == colors[0] for color in colors):
            colors[-1] = (colors[0] + 1) % 101
        cases.add(tuple(colors))
    generated_calls = [f"candidate(colors={list(a)!r})" for a in cases]
    example_calls = [
        "candidate(colors=[1, 1, 1, 6, 1, 1, 1])",
        "candidate(colors=[1, 8, 3, 8, 3])",
        "candidate(colors=[0, 1])",
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
