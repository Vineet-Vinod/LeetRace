import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Complete binary trees with 1..100 nodes and values in [-1000,1000]."""
    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        count = rng.randint(1, 100)
        values = tuple(rng.randint(-1000, 1000) for _ in range(count))
        cases.add(values)
    calls = [f"candidate(root=tree_node({list(values)!r}))" for values in cases]
    calls.append(f"candidate(root=tree_node({list(range(10000))!r}))")
    calls.append(f"candidate(root=tree_node({[2**31 - 1, -(2**31), 2**31 - 1]!r}))")
    generated_calls = calls
    example_calls = [
        "candidate(root=tree_node([3, 9, 20, None, None, 15, 7]))",
        "candidate(root=tree_node([3, 9, 20, 15, 7]))",
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
