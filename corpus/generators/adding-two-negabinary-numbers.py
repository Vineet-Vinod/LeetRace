import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], tuple[int, ...]]] = {
        ((0,), (0,)),
        ((1,), (1,)),
        ((1, 1, 1, 1, 1), (1, 0, 1)),
    }
    while len(cases) < 600:
        a = rng.randint(1, 10**80)
        b = rng.randint(1, 10**80)

        def digits(value: int) -> tuple[int, ...]:
            result: list[int] = []
            while value:
                value, bit = divmod(value, -2)
                if bit < 0:
                    value += 1
                    bit = 1
                result.append(bit)
            return tuple(reversed(result or [0]))

        cases.add((digits(a), digits(b)))
    return [f"candidate(arr1={list(a)!r}, arr2={list(b)!r})" for a, b in cases]
