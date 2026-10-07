import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: money in [1,200], children in [2,30]."""
    rng = random.Random(seed)
    cases = {(rng.randint(1, 200), rng.randint(2, 30)) for _ in range(1000)}
    cases.update({(1, 2), (1, 30), (200, 2), (200, 30)})
    while len(cases) < 700:
        cases.add((rng.randint(1, 200), rng.randint(2, 30)))
    generated_calls = [f"candidate(money={m}, children={c})" for m, c in sorted(cases)]
    example_calls = [
        "candidate(money=20, children=3)",
        "candidate(money=16, children=2)",
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
