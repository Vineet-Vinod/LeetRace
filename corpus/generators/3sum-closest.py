def generate(seed: int = 0) -> list[str]:
    import itertools
    import random

    rng = random.Random(seed)
    cases = set()
    fixed = [([-1, 2, 1, -4], 1), ([0, 0, 0], 1), ([-2, 0, 1, 3], 1)]
    for nums, target in fixed:
        cases.add(f"candidate(nums={nums!r}, target={target})")
    cases.add(f"candidate(nums={[0] * 500!r}, target=0)")
    cases.add("candidate(nums=[-1000, 1000, 1000], target=10000)")
    cases.add("candidate(nums=[-1000, 1000, 1000], target=-10000)")
    # Values and target stay within the published bounds; arrays always have >= 3 items.
    for index in range(600):
        size = 3 + index % 26
        nums = [rng.randint(-1000, 1000) for _ in range(size)]
        possible_sums = {sum(triple) for triple in itertools.combinations(nums, 3)}
        while True:
            target = rng.randint(-10000, 10000)
            distance = min(abs(total - target) for total in possible_sums)
            if sum(abs(total - target) == distance for total in possible_sums) == 1:
                break
        cases.add(f"candidate(nums={nums!r}, target={target})")
    if "3sum-closest" == "determine-color-of-a-chessboard-square":
        return [
            f"candidate(coordinates={chr(97 + col) + str(row)!r})"
            for col in range(8)
            for row in range(1, 9)
        ]
    if "3sum-closest" == "smallest-even-multiple":
        return [f"candidate(n={value})" for value in range(1, 151)]
    while len(cases) < 600:
        nums = [rng.randint(-1000, 1000) for _ in range(rng.randint(3, 12))]
        possible_sums = {sum(triple) for triple in itertools.combinations(nums, 3)}
        while True:
            target = rng.randint(-10000, 10000)
            distance = min(abs(total - target) for total in possible_sums)
            if sum(abs(total - target) == distance for total in possible_sums) == 1:
                break
        cases.add(f"candidate(nums={nums!r}, target={target})")
    return sorted(cases)
