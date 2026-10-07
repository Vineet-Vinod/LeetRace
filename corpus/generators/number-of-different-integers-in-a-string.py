import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Lowercase letters and digits, total length at most 1000."""
    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        pieces = []
        for _ in range(rng.randint(1, 40)):
            pieces.append(
                "".join(rng.choice("0123456789") for _ in range(rng.randint(1, 20)))
            )
            pieces.append(
                "".join(rng.choice("abcxyz") for _ in range(rng.randint(1, 5)))
            )
        cases.add("".join(pieces))
    calls = [f"candidate(word={w!r})" for w in cases]
    boundary = ("a1234567890" * 90) + "a123456789"
    calls.append(f"candidate(word={boundary!r})")
    generated_calls = calls
    example_calls = [
        "candidate(word='a123bc34d8ef34')",
        "candidate(word='leet1234code234')",
        "candidate(word='a1b01c001')",
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
