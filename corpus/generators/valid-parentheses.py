"""Seeded unique calls are constructed within the stated input constraints."""


def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    opening_to_closing = {"(": ")", "[": "]", "{": "}"}
    closing_to_opening = {close: open_ for open_, close in opening_to_closing.items()}

    def is_valid(value: str) -> bool:
        stack = []
        for char in value:
            if char in opening_to_closing:
                stack.append(char)
            elif not stack or stack.pop() != closing_to_opening[char]:
                return False
        return not stack

    def make_valid(pair_count: int) -> str:
        result = []
        stack = []
        opened = 0
        for _ in range(2 * pair_count):
            if opened < pair_count and (not stack or rng.random() < 0.55):
                opening = rng.choice(tuple(opening_to_closing))
                stack.append(opening)
                result.append(opening)
                opened += 1
            else:
                result.append(opening_to_closing[stack.pop()])
        return "".join(result)

    valid_cases = set()
    invalid_cases = set()
    while len(valid_cases) < 300 or len(invalid_cases) < 300:
        value = make_valid(rng.randint(1, 50))
        if len(valid_cases) < 300:
            valid_cases.add(f"candidate(s={value!r})")
        if len(invalid_cases) < 300:
            invalidation = rng.randrange(4)
            if invalidation == 0:
                invalid = value + rng.choice(tuple(closing_to_opening))
            elif invalidation == 1:
                invalid = rng.choice(tuple(closing_to_opening)) + value
            elif invalidation == 2:
                wrong_closers = tuple(
                    close for close in closing_to_opening if close != value[-1]
                )
                invalid = value[:-1] + rng.choice(wrong_closers)
            else:
                invalid = value[:-1]
            invalid_cases.add(f"candidate(s={invalid!r})")
    import ast

    assert all(
        is_valid(ast.literal_eval(call.split("s=", 1)[1][:-1])) for call in valid_cases
    )
    assert all(
        not is_valid(ast.literal_eval(call.split("s=", 1)[1][:-1]))
        for call in invalid_cases
    )
    return sorted(valid_cases | invalid_cases)


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(
        [
            "candidate(s='(' * 5000 + ')' * 5000)",
            "candidate(s=')' + '()' * 4999)",
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
            "candidate(s='(')",
            "candidate(s='()')",
            "candidate(s='()[]{}')",
            "candidate(s='(]')",
            "candidate(s='([])')",
        ]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
