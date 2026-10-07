"""Unique lowercase words have length 1..30 and there are at most 100; includes 100 distinct words and substring matches. Examples and prose use ascending lexicographic order."""

import ast
import random


def _calls(cases: list[dict[str, object]]) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for case in cases:
        arguments = ", ".join(f"{key}={value!r}" for key, value in case.items())
        call = f"candidate({arguments})"
        if call not in seen:
            seen.add(call)
            result.append(call)
    assert 500 <= len(result) <= 999, len(result)
    return result


EXAMPLE_CALLS = [
    "candidate(words=['mass', 'as', 'hero', 'superhero'])",
    "candidate(words=['leetcode', 'et', 'code'])",
    "candidate(words=['blue', 'green', 'bu'])",
]


def _with_examples(generated: list[str]) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for call in EXAMPLE_CALLS + generated:
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        if key not in seen:
            seen.add(key)
            result.append(call)
    assert 500 <= len(result) <= 999, len(result)
    return result


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[dict[str, object]] = []
    for _ in range(650):
        base = "".join(rng.choice("abc") for _ in range(rng.randint(4, 10)))
        words = list(dict.fromkeys([base, base[1:], base[:2]]))
        while len(words) < 4:
            word = "".join(rng.choice("xyz") for _ in range(rng.randint(1, 10)))
            if word not in words:
                words.append(word)
        calls.append({"words": words})
    calls.append(
        {
            "words": ["a" * i for i in range(1, 30)]
            + ["z" * 30]
            + [chr(97 + i // 26) + chr(97 + i % 26) for i in range(1, 71)]
        }
    )
    return _with_examples(_calls(calls))
