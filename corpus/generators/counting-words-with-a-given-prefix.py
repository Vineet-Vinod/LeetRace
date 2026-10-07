import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: 1..100 lowercase words and a lowercase prefix of length 1..100."""
    rng = random.Random(seed)
    cases = set()
    alphabet = "abc"
    while len(cases) < 600:
        words = tuple(
            "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 12)))
            for _ in range(rng.randint(1, 20))
        )
        pref = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 5)))
        cases.add((words, pref))
    calls = [f"candidate(words={list(w)!r}, pref={p!r})" for w, p in cases]
    words = ["a" * 100 for _ in range(100)]
    calls.append(f"candidate(words={words!r}, pref={'a' * 100!r})")
    generated_calls = calls
    example_calls = [
        "candidate(words=['pay', 'attention', 'practice', 'attend'], pref='at')",
        "candidate(words=['leetcode', 'win', 'loops', 'success'], pref='code')",
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
