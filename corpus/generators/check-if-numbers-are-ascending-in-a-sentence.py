import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate single-spaced sentences with strictly increasing and non-increasing positive numbers below 100."""
    rng = random.Random(seed)
    true_cases = set()
    false_cases = set()

    def sentence(numbers: list[int]) -> str:
        tokens = []
        for value in numbers:
            tokens.extend([rng.choice(("a", "cat", "word", "z")), str(value)])
        tokens.append(rng.choice(("a", "cat", "word", "z")))
        return " ".join(tokens)

    while len(true_cases) < 300:
        count = rng.randint(2, 10)
        values = sorted(rng.sample(range(1, 100), count))
        true_cases.add(sentence(values))
    while len(false_cases) < 300:
        count = rng.randint(2, 10)
        values = sorted(rng.sample(range(1, 100), count))
        if rng.random() < 0.5:
            values[-1] = values[-2]
        else:
            values[-2], values[-1] = values[-1], values[-2]
        false_cases.add(sentence(values))

    cases = (
        true_cases
        | false_cases
        | {
            "a 1 b 2",
            "a 2 b 2",
            "a 9 b 10 c 99",
            "x 99 y 1",
            "one 1 two 3",
        }
    )
    generated_calls = [f"candidate(s={value!r})" for value in cases]
    example_calls = [
        "candidate(s='1 box has 3 blue 4 red 6 green and 12 yellow marbles')",
        "candidate(s='hello world 5 x 5')",
        "candidate(s='sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s')",
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
