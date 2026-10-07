"""Each input is a directed line with one destination and unique alphabetic city labels of legal length."""

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
    "candidate(paths=[['London', 'New York'], ['New York', 'Lima'], ['Lima', 'Sao Paulo']])",
    "candidate(paths=[['B', 'C'], ['D', 'B'], ['C', 'A']])",
    "candidate(paths=[['A', 'Z']])",
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

    def pair(value: int) -> str:
        high, low = divmod(value, 26)
        return chr(ord("a") + high) + chr(ord("a") + low)

    for case_id in range(650):
        n = rng.randint(1, 50)
        prefix = pair(case_id)
        paths = [[prefix + pair(j), prefix + pair(j + 1)] for j in range(n)]
        calls.append({"paths": paths})
    calls.append(
        {
            "paths": [
                [
                    f"a{chr(97 + i // 26)}{chr(97 + i % 26)}",
                    f"a{chr(97 + (i + 1) // 26)}{chr(97 + (i + 1) % 26)}",
                ]
                for i in range(100)
            ]
        }
    )
    return _with_examples(_calls(calls))
