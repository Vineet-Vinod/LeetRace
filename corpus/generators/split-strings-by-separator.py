import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Nonempty strings and one-character separators from punctuation."""
    rng = random.Random(seed)
    cases = set()
    separators = ".,|$#@"
    while len(cases) < 600:
        sep = rng.choice(separators)
        words = tuple(
            "".join(
                rng.choice("abcdefghijklmnopqrstuvwxyz" + sep)
                for _ in range(rng.randint(1, 20))
            )
            for _ in range(rng.randint(1, 15))
        )
        cases.add((words, sep))
    generated_calls = [
        f"candidate(words={list(w)!r}, separator={s!r})" for w, s in cases
    ]
    example_calls = [
        "candidate(words=['one.two.three', 'four.five', 'six'], separator='.')",
        "candidate(words=['$easy$', '$problem$'], separator='$')",
        "candidate(words=['|||'], separator='|')",
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
