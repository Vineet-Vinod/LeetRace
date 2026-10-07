import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Length 1..50, values in [0,50], and k in [0,63]."""
    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        nums = tuple(rng.randint(0, 50) for _ in range(rng.randint(1, 50)))
        k = rng.randrange(64)
        cases.add((nums, k))
    generated_calls = [f"candidate(nums={list(a)!r}, k={k})" for a, k in cases]
    example_calls = [
        "candidate(nums=[1, 2, 3], k=2)",
        "candidate(nums=[2, 1, 8], k=10)",
        "candidate(nums=[1, 2], k=0)",
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
