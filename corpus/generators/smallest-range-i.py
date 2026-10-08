import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Nonempty arrays and k in [0,1000]."""
    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        nums = tuple(rng.randint(0, 1000) for _ in range(rng.randint(1, 100)))
        k = rng.randint(0, 1000)
        cases.add((nums, k))
    calls = [f"candidate(nums={list(a)!r}, k={k})" for a, k in cases]
    calls.append(f"candidate(nums={[0] * 9999 + [10000]!r}, k=10000)")
    generated_calls = calls
    example_calls = [
        "candidate(nums=[1], k=0)",
        "candidate(nums=[0, 10], k=2)",
        "candidate(nums=[1, 3, 6], k=3)",
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
