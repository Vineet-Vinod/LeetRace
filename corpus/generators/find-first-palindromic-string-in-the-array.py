def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        ("abc", "car", "ada", "racecar", "cool"),
        ("notapalindrome", "racecar"),
        ("def", "ghi"),
        tuple(["a" * 100] * 99 + ["b" * 100]),
    }
    while len(cases) < 600:
        words = []
        for _ in range(rng.randint(1, 20)):
            n = rng.randint(1, 20)
            word = "".join(rng.choice("abcxyz") for _ in range(n))
            if rng.random() < 0.25:
                half = word[: (n + 1) // 2]
                word = half + (half[:-1] if n % 2 else half)[::-1]
            words.append(word)
        cases.add(tuple(words))
    return [f"candidate(words={list(words)!r})" for words in sorted(cases)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(words=['abc', 'car', 'ada', 'racecar', 'cool'])",
    "candidate(words=['notapalindrome', 'racecar'])",
    "candidate(words=['def', 'ghi'])",
]
_ORIGINAL_GENERATE = generate


def generate(seed: int = 0) -> list[str]:
    import ast

    calls = _ORIGINAL_GENERATE(seed) + _STATEMENT_EXAMPLE_CALLS
    unique = {}
    for call in calls:
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        unique.setdefault(key, call)
    return [unique[key] for key in sorted(unique)]
