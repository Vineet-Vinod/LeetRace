import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Nonempty binary strings, length at most 50."""
    rng = random.Random(seed)
    cases = {"0", "1", "01", "0011", "01000111"}
    while len(cases) < 600:
        cases.add("".join(rng.choice("01") for _ in range(rng.randint(1, 50))))
    generated_calls = [f"candidate(s={s!r})" for s in cases]
    example_calls = ["candidate(s='00111')"]
    generated_calls.extend(example_calls)
    unique_calls = []
    seen_calls = set()
    for generated_call in generated_calls:
        key = ast.dump(ast.parse(generated_call, mode="eval"), include_attributes=False)
        if key not in seen_calls:
            seen_calls.add(key)
            unique_calls.append(generated_call)
    return unique_calls
