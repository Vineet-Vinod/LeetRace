import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        nums = rng.sample(range(1, 10**9), rng.randint(1, 40))
        occupied = set(nums)
        move_from, move_to = [], []
        for _ in range(rng.randint(1, 40)):
            source = rng.choice(tuple(occupied))
            target = rng.randint(1, 10**9)
            move_from.append(source)
            move_to.append(target)
            occupied.remove(source)
            occupied.add(target)
        calls.add(
            f"candidate(nums={nums!r}, moveFrom={move_from!r}, moveTo={move_to!r})"
        )
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(nums=[1, 1, 3, 3], moveFrom=[1, 3], moveTo=[2, 2])",
    "candidate(nums=[1, 6, 7, 8], moveFrom=[1, 7, 2], moveTo=[2, 9, 5])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
