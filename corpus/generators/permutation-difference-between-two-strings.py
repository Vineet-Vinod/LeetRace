import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Distinct lowercase characters; t is a permutation of s."""
    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        s = "".join(rng.sample("abcdefghijklmnopqrstuvwxyz", rng.randint(1, 26)))
        t = list(s)
        rng.shuffle(t)
        cases.add((s, "".join(t)))
    generated_calls = [f"candidate(s={s!r}, t={t!r})" for s, t in cases]
    example_calls = ["candidate(s='abc', t='bac')", "candidate(s='abcde', t='edbac')"]
    generated_calls.extend(example_calls)
    unique_calls = []
    seen_calls = set()
    for generated_call in generated_calls:
        key = ast.dump(ast.parse(generated_call, mode="eval"), include_attributes=False)
        if key not in seen_calls:
            seen_calls.add(key)
            unique_calls.append(generated_call)
    return unique_calls
