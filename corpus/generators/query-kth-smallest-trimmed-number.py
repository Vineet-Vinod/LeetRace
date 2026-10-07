import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[str, ...], tuple[tuple[int, int], ...]]] = {
        (("102", "473", "251", "814"), ((1, 1), (2, 3), (4, 2), (1, 2))),
        (("001", "001", "100"), ((1, 3), (2, 3), (3, 1))),
        (("0" * 100,) * 100, ((1, 100),) * 100),
    }
    digits = 12
    while len(cases) < 600:
        count = rng.randint(1, 30)
        nums = tuple(
            "".join(rng.choice("0123456789") for _ in range(digits))
            for _ in range(count)
        )
        queries = tuple(
            (rng.randint(1, count), rng.randint(1, digits))
            for _ in range(rng.randint(1, 30))
        )
        cases.add((nums, queries))
    assert all(
        1 <= len(nums) <= 100
        and 1 <= len(nums[0]) <= 100
        and all(len(number) == len(nums[0]) and number.isdigit() for number in nums)
        and 1 <= len(queries) <= 100
        and all(
            1 <= rank <= len(nums) and 1 <= trim <= len(nums[0])
            for rank, trim in queries
        )
        for nums, queries in cases
    )
    return [
        f"candidate(nums={list(nums)!r}, queries={[list(q) for q in queries]!r})"
        for nums, queries in sorted(cases)
    ]
