import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Full binary trees whose parent value is the minimum of its children."""
    rng = random.Random(seed)

    def make(level: int) -> list[int]:
        size = 2**level - 1
        leaf_start = 2 ** (level - 1) - 1
        values = [0] * size
        for i in range(leaf_start, size):
            values[i] = rng.randint(1, 2**31 - 1)
        for i in range(leaf_start - 1, -1, -1):
            values[i] = min(values[2 * i + 1], values[2 * i + 2])
        return values

    cases = set()
    while len(cases) < 600:
        level = rng.randint(1, 4)
        cases.add(tuple(make(level)))
    values = [0] * 25
    leaves = [2**31 - 1, 1, *range(2, 13)]
    values[12:] = leaves
    for index in range(11, -1, -1):
        values[index] = min(values[2 * index + 1], values[2 * index + 2])
    calls = [f"candidate(root=tree_node({list(v)!r}))" for v in cases]
    calls.append(f"candidate(root=tree_node({values!r}))")
    generated_calls = calls
    example_calls = [
        "candidate(root=tree_node([2, 2, 5, None, None, 5, 7]))",
        "candidate(root=tree_node([2, 2, 2]))",
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
