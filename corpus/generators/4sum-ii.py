import random


def generate(seed: int = 0) -> list[str]:
    """Create 600 distinct valid calls; arrays share n and values stay in [-2^28, 2^28]."""
    rng = random.Random(seed)
    cases: list[str] = []
    seen: set[str] = set()
    index = 0
    while len(cases) < 600:
        n = index % 8 + 1
        arrays = [[rng.randint(-50, 50) for _ in range(n)] for _ in range(4)]
        if index % 3 == 0:
            arrays[3][-1] = -sum(arrays[j][0] for j in range(3))
        assert all(
            1 <= len(a) <= 200 and all(-(2**28) <= x <= 2**28 for x in a)
            for a in arrays
        )
        call = (
            "candidate("
            + ", ".join(f"nums{j + 1}={a!r}" for j, a in enumerate(arrays))
            + ")"
        )
        index += 1
        if call not in seen:
            seen.add(call)
            cases.append(call)
    return cases
