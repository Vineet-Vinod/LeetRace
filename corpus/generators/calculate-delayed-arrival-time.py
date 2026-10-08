"""All 23 legal arrival hours paired with all 24 legal delays are enumerated (552 distinct legal inputs)."""

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


EXAMPLE_CALLS = [
    "candidate(arrivalTime=15, delayedTime=5)",
    "candidate(arrivalTime=13, delayedTime=11)",
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
    random.Random(seed)
    calls = [
        {"arrivalTime": a, "delayedTime": d} for a in range(1, 24) for d in range(1, 25)
    ]
    calls.extend(
        [{"arrivalTime": 23, "delayedTime": 24}, {"arrivalTime": 1, "delayedTime": 1}]
    )
    return _with_examples(_calls(calls))
