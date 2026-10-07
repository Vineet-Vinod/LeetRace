import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate positive integers in [1, 10^8], including both numeric bounds."""
    rng = random.Random(seed)
    values = set(range(1, 201))
    values.update({10**8, 10**8 - 1})
    while len(values) < 700:
        values.add(rng.randint(1, 10**8))
    generated_calls = [f"candidate(num={number})" for number in sorted(values)]
    example_calls = ["candidate(num=11891)"]
    generated_calls.extend(example_calls)
    unique_calls = []
    seen_calls = set()
    for generated_call in generated_calls:
        key = ast.dump(ast.parse(generated_call, mode="eval"), include_attributes=False)
        if key not in seen_calls:
            seen_calls.add(key)
            unique_calls.append(generated_call)
    return unique_calls
