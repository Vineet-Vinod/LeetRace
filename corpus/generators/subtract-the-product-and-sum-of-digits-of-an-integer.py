import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: n in [1,10^6]."""
    rng = random.Random(seed)
    values = set(range(1, 501))
    while len(values) < 600:
        values.add(rng.randint(1, 10**5))
    generated_calls = [f"candidate(n={n})" for n in values]
    example_calls = ["candidate(n=4421)"]
    generated_calls.extend(example_calls)
    unique_calls = []
    seen_calls = set()
    for generated_call in generated_calls:
        key = ast.dump(ast.parse(generated_call, mode="eval"), include_attributes=False)
        if key not in seen_calls:
            seen_calls.add(key)
            unique_calls.append(generated_call)
    return unique_calls
