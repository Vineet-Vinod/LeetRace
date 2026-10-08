import random


def generate(seed: int = 0) -> list[str]:
    """Generate even arrays of length 2..30000 and values -100000..100000."""
    rng = random.Random(seed)
    calls = {
        "candidate(arr=[3, 1, 3, 6])",
        "candidate(arr=[4, -2, 2, -4])",
        "candidate(arr=[0] * 30000)",
        "candidate(arr=[0] * 29998 + [1, 1])",
    }
    while len(calls) < 600:
        pair_count = rng.randint(1, 40)
        if rng.random() < 0.55:
            arr: list[int] = []
            for _ in range(pair_count):
                value = rng.randint(-50_000, 50_000)
                arr.extend((value, 2 * value))
            rng.shuffle(arr)
        else:
            arr = [rng.randint(-100, 100) for _ in range(2 * pair_count)]
        assert 2 <= len(arr) <= 30_000 and len(arr) % 2 == 0
        assert all(-100_000 <= value <= 100_000 for value in arr)
        calls.add(f"candidate(arr={arr!r})")
    return sorted(calls)
