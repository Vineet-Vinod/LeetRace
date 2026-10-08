"""Valid level-order trees have 0..5000 nodes and values in [-10^4,10^4]; includes maximum node count and 144 left-skewed unbalanced cases."""

import ast
import random


def _calls(cases: list[dict[str, object]]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for case in cases:
        args = ", ".join(f"{key}={value!r}" for key, value in case.items())
        call = f"candidate({args})"
        if call not in seen:
            seen.add(call)
            out.append(call)
    assert len(out) >= 500, len(out)
    assert len(out) <= 999, len(out)
    return out


def _tree_calls(arrays: list[list[int | None]]) -> list[str]:
    result = [f"candidate(root=tree_node({values!r}))" for values in arrays]
    result = list(dict.fromkeys(result))
    assert 500 <= len(result) <= 999
    return result


EXAMPLE_CALLS = [
    "candidate(root=tree_node([3, 9, 20, None, None, 15, 7]))",
    "candidate(root=tree_node([1, 2, 2, 3, 3, None, None, 4, 4]))",
    "candidate(root=tree_node([]))",
]


def _with_examples(generated: list[str]) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for call in EXAMPLE_CALLS + generated:
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        if key not in seen:
            seen.add(key)
            result.append(call)
    assert 500 <= len(result) <= 999, len(result)
    return result


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    arrays = [[], [1], [1, 2, 3], [1, 2, None, 3], [1, 2, None, 3, None, None, None, 4]]
    for _ in range(620):
        n = rng.randint(0, 45)
        values = [rng.randint(-10_000, 10_000) for _ in range(n)]
        arrays.append(values)
    arrays.append([1] * 5000)
    for depth in range(3, 9):
        for offset in range(24):
            values: list[int | None] = [None] * (2**depth - 1)
            index = 0
            for level in range(depth):
                values[index] = offset + level
                index = 2 * index + 1
            arrays.append(values)
    return _with_examples(_tree_calls(arrays))
