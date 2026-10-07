import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    targets = {2, 3, -2, -3}
    while len(targets) < 600:
        target = rng.randint(-(10**9), 10**9)
        if target:
            targets.add(target)
    return [f"candidate(target={target})" for target in targets]
