import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Square matrices of size 1..100 with values in [1,100]."""
    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 30)
        cases.add(tuple(tuple(rng.randint(1, 100) for _ in range(n)) for _ in range(n)))
    generated_calls = [f"candidate(mat={list(map(list, m))!r})" for m in cases]
    example_calls = [
        "candidate(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])",
        "candidate(mat=[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])",
        "candidate(mat=[[5]])",
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
