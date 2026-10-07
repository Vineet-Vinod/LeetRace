import random


def generate(seed: int = 0) -> list[str]:
    """Both arrays are nonempty and contain positive integers within the task's digit bound."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        arr1 = [rng.randrange(1, 10**8) for _ in range(1 + i % 18)]
        arr2 = [rng.randrange(1, 10**8) for _ in range(1 + (i * 7) % 18)]
        call = f"candidate(arr1={arr1!r}, arr2={arr2!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
