import ast
import random


def generate(seed: int = 0) -> list[str]:
    """Generate circular and non-circular sentences of English letters with single spaces."""
    rng = random.Random(seed)
    true_cases = set()
    false_cases = set()
    letters = "abCDxy"

    while len(true_cases) < 300:
        count = rng.randint(1, 8)
        links = [rng.choice(letters) for _ in range(count)]
        words = []
        for index in range(count):
            middle = "".join(rng.choice(letters) for _ in range(rng.randint(0, 6)))
            words.append(links[index - 1] + middle + links[index])
        true_cases.add(" ".join(words))

    while len(false_cases) < 300:
        words = [
            "".join(rng.choice(letters) for _ in range(rng.randint(1, 8)))
            for _ in range(rng.randint(1, 8))
        ]
        sentence = " ".join(words)
        if any(
            words[index][-1] != words[(index + 1) % len(words)][0]
            for index in range(len(words))
        ):
            false_cases.add(sentence)

    cases = true_cases | false_cases | {"a", "a a", "ab ba", "Leetcode is cool"}
    generated_calls = [f"candidate(sentence={sentence!r})" for sentence in cases]
    example_calls = [
        "candidate(sentence='leetcode exercises sound delightful')",
        "candidate(sentence='eetcode')",
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
