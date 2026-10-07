import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Dimensions in [1,100000] and mass in [1,1000]."""
    rng = random.Random(seed)
    cases = set()
    edges = [1, 99, 1000, 9999, 10000, 100000]
    for a in edges:
        for b in edges:
            for c in edges:
                for m in [1, 99, 100, 1000]:
                    cases.add((a, b, c, m))
    while len(cases) < 600:
        cases.add(
            (
                rng.randint(1, 100000),
                rng.randint(1, 100000),
                rng.randint(1, 100000),
                rng.randint(1, 1000),
            )
        )
    generated_calls = [
        f"candidate(length={a}, width={b}, height={c}, mass={m})"
        for a, b, c, m in sorted(cases)
    ]
    example_calls = [
        "candidate(length=1000, width=35, height=700, mass=300)",
        "candidate(length=200, width=50, height=800, mass=50)",
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
