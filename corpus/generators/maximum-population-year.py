import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Nonempty logs with 1950 <= birth < death <= 2050."""
    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        logs = tuple(
            sorted(
                (a := rng.randint(1950, 2049), rng.randint(a + 1, 2050))
                for _ in range(rng.randint(1, 100))
            )
        )
        cases.add(logs)
    calls = [f"candidate(logs={list(map(list, logs))!r})" for logs in cases]
    calls.append(f"candidate(logs={[[1950, 2050]] * 100!r})")
    calls.append(
        f"candidate(logs={[[1950 + index, 1951 + index] for index in range(100)]!r})"
    )
    generated_calls = calls
    example_calls = [
        "candidate(logs=[[1993, 1999], [2000, 2010]])",
        "candidate(logs=[[1950, 1961], [1960, 1971], [1970, 1981]])",
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
