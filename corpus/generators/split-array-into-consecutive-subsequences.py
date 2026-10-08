import random


def generate(seed: int = 0) -> list[str]:
    """Create 300 partitionable unions and 300 inputs with an impossible suffix."""
    rng = random.Random(seed)
    calls: set[str] = set()
    true_calls: set[str] = set()
    false_calls: set[str] = set()

    # Repeating every value in a run m times gives m disjoint valid subsequences.
    while len(true_calls) < 300:
        values = []
        group_count = 1 + rng.randrange(5)
        for _ in range(group_count):
            start = rng.randint(-1000, 988)
            length = 3 + rng.randrange(10)
            copies = 1 + rng.randrange(3)
            values.extend(
                value for value in range(start, start + length) for _ in range(copies)
            )
        values.sort()
        assert 1 <= len(values) <= 10_000
        assert all(-1000 <= value <= 1000 for value in values)
        true_calls.add(f"candidate(nums={values!r})")

    # Each x..x+2 has k copies, but x+3 has k+1; its final copy cannot belong
    # to any valid consecutive subsequence. Vary x and k for distinct cases.
    while len(false_calls) < 300:
        start = rng.randint(-996, 996)
        copies = 1 + rng.randrange(300)
        values = [start] * copies + [start + 1] * copies + [start + 2] * copies
        values.extend([start + 3] * (copies + 1))
        values.sort()
        assert 1 <= len(values) <= 10_000
        assert all(-1000 <= value <= 1000 for value in values)
        false_calls.add(f"candidate(nums={values!r})")

    calls.update(true_calls)
    calls.update(false_calls)

    # Exact maximum-size valid and invalid boundaries; the valid runs are
    # [-1000..1000] twice, [-1000..997] three times, and [997..1000] once.
    maximum_valid = list(range(-1000, 1001)) * 2
    maximum_valid.extend(list(range(-1000, 998)) * 3)
    maximum_valid.extend(range(997, 1001))
    maximum_valid.sort()
    assert len(maximum_valid) == 10_000
    assert all(-1000 <= value <= 1000 for value in maximum_valid)
    calls.add(f"candidate(nums={maximum_valid!r})")

    # This size-10000 input includes both value endpoints. The separated
    # three-value prefix is feasible, while the x..x+3 component is not.
    copies = 2499
    maximum_invalid = [-1000, -999, -998]
    maximum_invalid.extend([997] * copies)
    maximum_invalid.extend([998] * copies)
    maximum_invalid.extend([999] * copies)
    maximum_invalid.extend([1000] * (copies + 1))
    assert len(maximum_invalid) == 10_000
    assert all(-1000 <= value <= 1000 for value in maximum_invalid)
    calls.add(f"candidate(nums={maximum_invalid!r})")

    assert len(true_calls) == 300 and len(false_calls) == 300
    assert len(calls) == 602
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(nums=[1, 2, 3, 3, 4, 5])",
    "candidate(nums=[1, 2, 3, 4, 4, 5])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
