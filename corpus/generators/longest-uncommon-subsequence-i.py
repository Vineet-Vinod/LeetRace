import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Nonempty lowercase strings of length at most 100."""
    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        a = "".join(rng.choice("abc") for _ in range(rng.randint(1, 100)))
        b = (
            a
            if rng.random() < 0.25
            else "".join(rng.choice("abc") for _ in range(rng.randint(1, 100)))
        )
        cases.add((a, b))
    calls = [f"candidate(a={a!r}, b={b!r})" for a, b in cases]
    boundary = "a" * 100
    calls.append(f"candidate(a={boundary!r}, b={('a' * 99 + 'b')!r})")
    generated_calls = calls
    example_calls = [
        "candidate(a='aba', b='cdc')",
        "candidate(a='aaa', b='bbb')",
        "candidate(a='aaa', b='aaa')",
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
