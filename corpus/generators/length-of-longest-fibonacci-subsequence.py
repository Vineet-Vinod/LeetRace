def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    fib = [1, 2]
    while fib[-1] + fib[-2] <= 10**9:
        fib.append(fib[-1] + fib[-2])
    maximum = fib + sorted(rng.sample(range(fib[-1] + 1, 10**9 + 1), 1000 - len(fib)))
    cases = {
        f"candidate(arr={fib!r})",
        f"candidate(arr={maximum!r})",
        "candidate(arr=[1,2,3,1000000000])",
    }
    while len(cases) < 600:
        if rng.random() < 0.5:
            length = rng.randint(3, len(fib))
            arr = fib[:length]
            if rng.random() < 0.5:
                extra = sorted(
                    rng.sample(range(fib[-1] + 1, 10**9 + 1), rng.randint(1, 20))
                )
                arr += extra
        else:
            scale = rng.randint(1, 1000)
            length = rng.randint(3, 20)
            arr = [scale * (1 << bit) for bit in range(length)]
        assert 3 <= len(arr) <= 1000
        assert all(
            1 <= arr[index] < arr[index + 1] <= 10**9 for index in range(len(arr) - 1)
        )
        cases.add(f"candidate(arr={arr!r})")
    return sorted(cases)
