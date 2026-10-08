import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Nonempty integer arrays."""
    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        nums = tuple(rng.randint(-1000, 1000) for _ in range(rng.randint(1, 100)))
        cases.add(nums)
    cases.update({(1,), (1, 2), (1, 2, 3), (2, 2, 3, 1)})
    calls = [f"candidate(nums={list(a)!r})" for a in cases]
    calls.append(f"candidate(nums={[-(2**31), 2**31 - 1, 0]!r})")
    generated_calls = calls
    example_calls = ["candidate(nums=[3, 2, 1])"]
    generated_calls.extend(example_calls)
    unique_calls = []
    seen_calls = set()
    for generated_call in generated_calls:
        key = ast.dump(ast.parse(generated_call, mode="eval"), include_attributes=False)
        if key not in seen_calls:
            seen_calls.add(key)
            unique_calls.append(generated_call)
    return unique_calls
