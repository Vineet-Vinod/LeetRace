import random


_MAX_LENGTH = 10_000
_MAX_VALUE = 1000


def generate(seed: int = 0) -> list[str]:
    """Every array has length 1..10^4 and all values are in [2, 1000]."""
    rng = random.Random(seed)
    calls = {
        "candidate(nums=[2, 4, 3, 7, 10, 6])",
        "candidate(nums=[2, 4, 8, 16])",
        "candidate(nums=[2])",
        f"candidate(nums={[2 + index % 999 for index in range(_MAX_LENGTH)]!r})",
        f"candidate(nums={[_MAX_VALUE] * _MAX_LENGTH!r})",
    }
    while len(calls) < 600:
        length = rng.randint(1, 100)
        values = [rng.randint(2, _MAX_VALUE) for _ in range(length)]
        calls.add(f"candidate(nums={values!r})")
    for call in calls:
        import ast

        values = ast.literal_eval(ast.parse(call, mode="eval").body.keywords[0].value)
        assert 1 <= len(values) <= _MAX_LENGTH
        assert all(2 <= value <= _MAX_VALUE for value in values)
    return sorted(calls)
