"""Graphs use 1..45 vertices, unique non-self undirected edges, and valid source/destination labels."""

import ast
import random


def _calls(cases: list[dict[str, object]]) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for case in cases:
        arguments = ", ".join(f"{key}={value!r}" for key, value in case.items())
        call = f"candidate({arguments})"
        if call not in seen:
            seen.add(call)
            result.append(call)
    assert 500 <= len(result) <= 999, len(result)
    return result


EXAMPLE_CALLS = [
    "candidate(n=3, edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2)",
    "candidate(n=6, edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source=0, destination=5)",
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
    calls: list[dict[str, object]] = []
    for _ in range(650):
        n = rng.randint(1, 45)
        edges = [[i, i + 1] for i in range(n - 1) if rng.random() < 0.7]
        edges += [
            [a, b] for a in range(n) for b in range(a + 2, n) if rng.random() < 0.025
        ]
        calls.append(
            {
                "n": n,
                "edges": edges,
                "source": rng.randrange(n),
                "destination": rng.randrange(n),
            }
        )
    calls.append({"n": 200_000, "edges": [], "source": 0, "destination": 199_999})
    return _with_examples(_calls(calls))
