import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: dict[str, str] = {}

    def add(nums: list[int]) -> None:
        assert 1 <= len(nums) <= 100_000
        assert all(value in (0, 1) for value in nums)
        call = f"candidate(nums={nums!r})"
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        cases.setdefault(key, call)

    add([0])
    add([0, 1, 1, 1])
    add([1, 0, 1, 0])
    add([0] * 100_000)
    add([index % 2 for index in range(100_000)])
    while len(cases) < 600:
        size = rng.randint(1, 100)
        add([rng.randint(0, 1) for _ in range(size)])
    assert len(cases) == len(set(cases)) and len(cases) >= 600
    return sorted(cases.values())
