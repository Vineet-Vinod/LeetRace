"""Pattern length is at most 300; lowercase sentence length is at most 3000 with no edge spaces. Includes 250 generated bijections and maximum-length boundary cases."""

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
    "candidate(pattern='abba', s='dog cat cat dog')",
    "candidate(pattern='abba', s='dog cat cat fish')",
    "candidate(pattern='aaaa', s='dog cat cat dog')",
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
        pattern = "".join(rng.choice("abcd") for _ in range(rng.randint(1, 20)))
        words = [rng.choice("wxyz") for _ in pattern]
        calls.append({"pattern": pattern, "s": " ".join(words)})
    for _ in range(250):
        pattern = "".join(rng.choice("abcd") for _ in range(rng.randint(1, 30)))
        mapping = {
            letter: chr(97 + index) * 3
            for index, letter in enumerate(sorted(set(pattern)))
        }
        sentence = " ".join(mapping[letter] for letter in pattern)
        calls.append({"pattern": pattern, "s": sentence})
    calls.append({"pattern": "a" * 300, "s": ("abcdefgh " * 299) + "abcdefgh"})
    return _with_examples(_calls(calls))
