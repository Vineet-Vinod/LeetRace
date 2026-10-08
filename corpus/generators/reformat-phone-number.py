import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Phone strings with 2..100 digits separated only by spaces or dashes."""
    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(2, 50)
        digits = "".join(rng.choice("0123456789") for _ in range(n))
        decorated = "".join(
            ch + (rng.choice(["", " ", "-"]) if i < n - 1 else "")
            for i, ch in enumerate(digits)
        )
        cases.add(decorated)
    generated_calls = [f"candidate(number={s!r})" for s in cases]
    example_calls = [
        "candidate(number='1-23-45 6')",
        "candidate(number='123 4-567')",
        "candidate(number='123 4-5678')",
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
