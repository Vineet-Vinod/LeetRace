import random


def generate(seed: int = 0) -> list[str]:

    rng = random.Random(seed)
    values = set(range(1, 401))
    values.update(rng.sample(range(401, 1001), 200))
    return [f"candidate(n={n})" for n in sorted(values)]
