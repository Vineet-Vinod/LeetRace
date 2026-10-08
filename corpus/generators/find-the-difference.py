import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Lowercase s of length 0..1000; t is a shuffled s plus one lowercase letter."""
    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        s = "".join(rng.choice("abcdef") for _ in range(rng.randint(0, 100)))
        chars = list(s + rng.choice("abcdef"))
        rng.shuffle(chars)
        cases.add((s, "".join(chars)))
    generated_calls = [f"candidate(s={s!r}, t={t!r})" for s, t in cases]
    example_calls = ["candidate(s='abcd', t='abcde')", "candidate(s='', t='y')"]
    generated_calls.extend(example_calls)
    unique_calls = []
    seen_calls = set()
    for generated_call in generated_calls:
        key = ast.dump(ast.parse(generated_call, mode="eval"), include_attributes=False)
        if key not in seen_calls:
            seen_calls.add(key)
            unique_calls.append(generated_call)
    return unique_calls
