import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    true_cases: set[str] = set()
    false_cases: set[str] = set()

    while len(true_cases) < 300:
        size = rng.randint(3, 1000)
        arr = [rng.randint(1, 1000) for _ in range(size)]
        start = rng.randint(0, size - 3)
        arr[start : start + 3] = [rng.randrange(1, 1001, 2) for _ in range(3)]
        assert any(
            arr[i] % 2 and arr[i + 1] % 2 and arr[i + 2] % 2 for i in range(size - 2)
        )
        true_cases.add(f"candidate(arr={arr!r})")

    while len(false_cases) < 300:
        size = rng.randint(1, 1000)
        arr: list[int] = []
        while len(arr) < size:
            odd_count = rng.randint(0, 2)
            arr.extend(
                rng.randrange(1, 1001, 2)
                for _ in range(min(odd_count, size - len(arr)))
            )
            if len(arr) < size:
                arr.append(rng.randrange(2, 1001, 2))
        arr = arr[:size]
        assert not any(
            arr[i] % 2 and arr[i + 1] % 2 and arr[i + 2] % 2 for i in range(size - 2)
        )
        false_cases.add(f"candidate(arr={arr!r})")

    return sorted(true_cases | false_cases)
