import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Unsigned 32-bit integers."""
    rng = random.Random(seed)
    values = set(range(512))
    while len(values) < 600:
        values.add(rng.randrange(2**32))
    values.update({0, 1, 2**31, 2**32 - 1})
    generated_calls = [f"candidate(n={n})" for n in values]
    example_calls = ["candidate(n=43261596)", "candidate(n=4294967293)"]
    generated_calls.extend(example_calls)
    unique_calls = []
    seen_calls = set()
    for generated_call in generated_calls:
        key = ast.dump(ast.parse(generated_call, mode="eval"), include_attributes=False)
        if key not in seen_calls:
            seen_calls.add(key)
            unique_calls.append(generated_call)
    return unique_calls
