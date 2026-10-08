import random


def generate(seed: int = 0) -> list[str]:
    """Generate duplicate pairs inside and outside k, plus unique arrays, within stated integer and size bounds."""
    rng = random.Random(seed)
    true_cases = set()
    false_cases = set()

    while len(true_cases) < 300:
        length = rng.randint(2, 80)
        values = [rng.randint(-1000, 1000) for _ in range(length)]
        first = rng.randrange(length - 1)
        second = rng.randint(first + 1, length - 1)
        values[second] = values[first]
        k = rng.randint(second - first, 100000)
        true_cases.add((tuple(values), k))
    while len(false_cases) < 300:
        length = rng.randint(1, 80)
        values = tuple(rng.sample(range(-1000000, 1000001), length))
        false_cases.add((values, rng.randint(0, 100000)))

    cases = (
        true_cases
        | false_cases
        | {
            ((1, 2, 3, 1), 3),
            ((1, 0, 1, 1), 1),
            ((1, 2, 3, 1, 2, 3), 2),
            ((-1000000000, 0, -1000000000), 2),
        }
    )
    calls = [f"candidate(nums={list(values)!r}, k={k})" for values, k in cases]
    boundary = list(range(100000))
    boundary[-1] = boundary[0]
    calls.append(f"candidate(nums={boundary!r}, k=99999)")
    return calls
