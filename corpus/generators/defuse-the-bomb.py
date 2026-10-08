import random


def generate(seed: int = 0) -> list[str]:
    """All generated arguments stay within the statement bounds and follow the problem guarantees."""
    r = random.Random(seed)
    cases = [([5, 7, 1, 4], 3), ([1, 2, 3, 4], 0)]
    seen = {(tuple(a), k) for a, k in cases}
    while len(cases) < 600:
        a = [r.randint(1, 100) for _ in range(r.randint(1, 30))]
        k = r.randint(-(len(a) - 1), len(a) - 1)
        key = (tuple(a), k)
        if key not in seen:
            seen.add(key)
            cases.append((a, k))
    return [f"candidate(code={a!r}, k={k})" for a, k in cases]


_BASE_GENERATE = generate
_BOUNDARY_CALLS = [
    "candidate(code=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100], k=99)",
    "candidate(code=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100], k=-99)",
]


def generate(seed: int = 0) -> list[str]:
    calls = _BASE_GENERATE(seed)
    return calls + [call for call in _BOUNDARY_CALLS if call not in calls]


_EXAMPLE_CALLS = ["candidate(code=[2, 4, 9, 3], k=-2)"]

_PREVIOUS_GENERATE = generate


def generate(seed: int = 0) -> list[str]:
    calls = _PREVIOUS_GENERATE(seed)
    return calls + [call for call in _EXAMPLE_CALLS if call not in calls]
