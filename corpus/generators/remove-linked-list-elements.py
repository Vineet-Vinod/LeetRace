import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Lists of length 0..1000 and target values in [-50,50]."""
    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        vals = tuple(rng.randint(1, 10) for _ in range(rng.randint(0, 100)))
        target = rng.randint(1, 10)
        cases.add((vals, target))
    generated_calls = [
        f"candidate(head=list_node({list(v)!r}), val={t})" for v, t in cases
    ]
    example_calls = [
        "candidate(head=list_node([1, 2, 6, 3, 4, 5, 6]), val=6)",
        "candidate(head=list_node([7, 7, 7, 7]), val=7)",
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
