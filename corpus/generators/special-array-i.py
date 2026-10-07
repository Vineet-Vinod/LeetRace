"""Seeded unique calls are constructed within the stated input constraints."""


def _generate_current(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    valid_cases = {
        "candidate(nums=" + repr([1, 2] * 50) + ")",
        "candidate(nums=[100, 99])",
    }
    invalid_cases = {
        "candidate(nums=" + repr([1, 3] + [2, 1] * 49) + ")",
        "candidate(nums=[100, 98])",
    }

    def is_special(nums: list[int]) -> bool:
        return all((left - right) % 2 != 0 for left, right in zip(nums, nums[1:]))

    while len(valid_cases) < 300 or len(invalid_cases) < 300:
        size = rng.randint(1, 100)
        nums = [
            rng.choice((2, 4, 6, 8, 10)) if (i % 2) else rng.choice((1, 3, 5, 7, 9))
            for i in range(size)
        ]
        if len(valid_cases) < 300:
            valid_cases.add(f"candidate(nums={nums!r})")
        if len(invalid_cases) < 300 and len(nums) >= 2:
            broken = nums.copy()
            index = rng.randrange(1, len(broken))
            previous_parity = broken[index - 1] % 2
            choices = [value for value in range(1, 101) if value % 2 == previous_parity]
            broken[index] = rng.choice(choices)
            invalid_cases.add(f"candidate(nums={broken!r})")
    assert all(is_special(ast_literal(call)) for call in valid_cases)
    assert all(not is_special(ast_literal(call)) for call in invalid_cases)
    return sorted(valid_cases | invalid_cases)


def ast_literal(call: str) -> list[int]:
    import ast

    return ast.literal_eval(call.split("nums=", 1)[1][:-1])


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(
        [
            "candidate(nums=[1])",
            "candidate(nums=[2, 1, 4])",
            "candidate(nums=[4, 3, 1, 6])",
        ]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
