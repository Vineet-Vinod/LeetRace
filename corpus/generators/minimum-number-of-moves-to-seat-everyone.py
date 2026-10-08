import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Equal nonempty arrays of length at most 100 with positions in [1,100]."""
    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 100)
        a = tuple(rng.randint(1, 100) for _ in range(n))
        b = tuple(rng.randint(1, 100) for _ in range(n))
        cases.add((a, b))
    calls = [f"candidate(seats={list(a)!r}, students={list(b)!r})" for a, b in cases]
    calls.append(
        f"candidate(seats={list(range(1, 101))!r}, students={list(range(100, 0, -1))!r})"
    )
    generated_calls = calls
    example_calls = [
        "candidate(seats=[3, 1, 5], students=[2, 7, 4])",
        "candidate(seats=[4, 1, 5, 9], students=[1, 3, 2, 6])",
        "candidate(seats=[2, 2, 6, 6], students=[1, 3, 2, 6])",
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
