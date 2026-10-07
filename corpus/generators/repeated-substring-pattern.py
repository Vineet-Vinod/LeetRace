"""Seeded unique calls are constructed within the stated input constraints."""


def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)

    def is_repeated(value: str) -> bool:
        prefix = [0] * len(value)
        for index in range(1, len(value)):
            match = prefix[index - 1]
            while match and value[index] != value[match]:
                match = prefix[match - 1]
            if value[index] == value[match]:
                match += 1
            prefix[index] = match
        period = len(value) - prefix[-1]
        return prefix[-1] > 0 and len(value) % period == 0

    repeated_cases = set()
    unique_marker_cases = set()
    while len(repeated_cases) < 300 or len(unique_marker_cases) < 300:
        pattern = "".join(rng.choice("abcd") for _ in range(rng.randint(1, 50)))
        copies = rng.randint(2, min(20, 10000 // len(pattern)))
        repeated_cases.add(f"candidate(s={pattern * copies!r})")
        left = rng.randint(1, 5000)
        right = rng.randint(1, 9999 - left)
        unique_marker = "a" * left + "b" + "c" * right
        unique_marker_cases.add(f"candidate(s={unique_marker!r})")
    import ast

    assert all(
        is_repeated(ast.literal_eval(call.split("s=", 1)[1][:-1]))
        for call in repeated_cases
    )
    assert all(
        not is_repeated(ast.literal_eval(call.split("s=", 1)[1][:-1]))
        for call in unique_marker_cases
    )
    return sorted(repeated_cases | unique_marker_cases)


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(
        [
            "candidate(s='ab' * 5000)",
            "candidate(s='a' * 9999 + 'b')",
        ]
    )
    for call in _generate_base(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(
        [
            "candidate(s='a')",
            "candidate(s='abab')",
            "candidate(s='aba')",
            "candidate(s='abcabcabcabc')",
        ]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
