import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Arrays of length 3..100 with values in [0,10^6]."""
    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(3, 100)
        cases.add(tuple(rng.randint(1, 10**6) for _ in range(n)))
    calls = [f"candidate(nums={list(a)!r})" for a in cases]
    calls.append(f"candidate(nums={[1, 10**6, 10**6]!r})")
    calls.append(f"candidate(nums={[10**6, 1, 10**6]!r})")
    generated_calls = calls
    example_calls = [
        "candidate(nums=[12, 6, 1, 2, 7])",
        "candidate(nums=[1, 10, 3, 4, 19])",
        "candidate(nums=[1, 2, 3])",
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
