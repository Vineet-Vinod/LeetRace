import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Distinct positive arrays of length 1..100."""
    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 100)
        a = tuple(rng.sample(range(1, 101), n))
        cases.add(a)
    cases.update({(1,), (1, 2), (1, 2, 3)})
    generated_calls = [f"candidate(nums={list(a)!r})" for a in cases]
    example_calls = ["candidate(nums=[3, 2, 1, 4])", "candidate(nums=[2, 1, 3])"]
    generated_calls.extend(example_calls)
    unique_calls = []
    seen_calls = set()
    for generated_call in generated_calls:
        key = ast.dump(ast.parse(generated_call, mode="eval"), include_attributes=False)
        if key not in seen_calls:
            seen_calls.add(key)
            unique_calls.append(generated_call)
    return unique_calls
