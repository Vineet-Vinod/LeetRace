import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Array lengths 1..100 and values in [1,100]."""
    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        a = tuple(rng.randint(1, 100) for _ in range(rng.randint(1, 60)))
        b = tuple(rng.randint(1, 100) for _ in range(rng.randint(1, 60)))
        cases.add((a, b))
    calls = [f"candidate(nums1={list(a)!r}, nums2={list(b)!r})" for a, b in cases]
    calls.append(
        f"candidate(nums1={list(range(1, 101))!r}, nums2={list(range(100, 0, -1))!r})"
    )
    generated_calls = calls
    example_calls = [
        "candidate(nums1=[2, 3, 2], nums2=[1, 2])",
        "candidate(nums1=[4, 3, 2, 3, 1], nums2=[2, 2, 5, 2, 3, 6])",
        "candidate(nums1=[3, 4, 2, 3], nums2=[1, 5])",
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
