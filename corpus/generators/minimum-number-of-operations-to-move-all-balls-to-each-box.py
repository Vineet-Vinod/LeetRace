def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(['candidate(boxes="110")', 'candidate(boxes="001011")'])
    for index in range(600):
        size = 2000 if index == 0 else 1 + index % 200
        boxes = "".join(rng.choice("01") for _ in range(size))
        cases.add(f"candidate(boxes={boxes!r})")
    return sorted(cases)
