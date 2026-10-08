import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Lowercase text and nonempty lowercase words."""
    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        text = "".join(rng.choice("abc") for _ in range(rng.randint(1, 60)))
        words = tuple(
            sorted(
                {
                    "".join(rng.choice("abc") for _ in range(rng.randint(1, 8)))
                    for _ in range(rng.randint(1, 8))
                }
            )
        )
        cases.add((text, words))
    calls = [f"candidate(text={t!r}, words={list(w)!r})" for t, w in cases]
    calls.append(
        f"candidate(text={'a' * 100!r}, words={[chr(97 + i) * 50 for i in range(20)]!r})"
    )
    generated_calls = calls
    example_calls = [
        "candidate(text='thestoryofleetcodeandme', words=['story', 'fleet', 'leetcode'])",
        "candidate(text='ababa', words=['aba', 'ab'])",
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
