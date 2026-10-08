import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Nonempty arrays with values in [1,100]."""
    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        nums = tuple(rng.randint(1, 50) for _ in range(rng.randint(1, 50)))
        cases.add(nums)
    calls = [f"candidate(nums={list(a)!r})" for a in cases]
    calls.append(f"candidate(nums={[50] * 50!r})")
    generated_calls = calls
    example_calls = [
        "candidate(nums=[1, 2, 3, 4])",
        "candidate(nums=[2, 7, 1, 19, 18, 3])",
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
