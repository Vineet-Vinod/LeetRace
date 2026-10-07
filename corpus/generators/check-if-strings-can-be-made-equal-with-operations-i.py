"""Both strings have length 4 and lowercase letters; random cases include 300 parity-preserving swaps to exercise true outcomes."""

import ast
import random
import string


def _calls(cases: list[dict[str, object]]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for case in cases:
        args = ", ".join(f"{key}={value!r}" for key, value in case.items())
        call = f"candidate({args})"
        if call not in seen:
            seen.add(call)
            out.append(call)
    assert len(out) >= 500, len(out)
    assert len(out) <= 999, len(out)
    return out


EXAMPLE_CALLS = ["candidate(s1='abcd', s2='cdab')", "candidate(s1='abcd', s2='dacb')"]


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
    calls = [{"s1": "abcd", "s2": "cdab"}, {"s1": "abcd", "s2": "dacb"}]
    for _ in range(620):
        s1 = "".join(rng.choice(string.ascii_lowercase) for _ in range(4))
        s2 = "".join(rng.choice(string.ascii_lowercase) for _ in range(4))
        calls.append({"s1": s1, "s2": s2})
    for _ in range(300):
        chars = [rng.choice(string.ascii_lowercase) for _ in range(4)]
        s1 = "".join(chars)
        if rng.randrange(2):
            chars[0], chars[2] = chars[2], chars[0]
        else:
            chars[1], chars[3] = chars[3], chars[1]
        calls.append({"s1": s1, "s2": "".join(chars)})
    return _with_examples(_calls(calls))
