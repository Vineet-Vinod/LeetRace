import random


_MAX_SUM = 2**31 - 1
_MAX_VALUE = 10**9
_MAX_LENGTH = 100_000


def generate(seed: int = 0) -> list[str]:
    """Nonnegative arrays satisfy the per-element and total-sum bounds; k is positive signed 32-bit."""
    rng = random.Random(seed)
    calls = {
        "candidate(nums=[23, 2, 4, 6, 7], k=6)",
        "candidate(nums=[23, 2, 6, 4, 7], k=6)",
        "candidate(nums=[23, 2, 6, 4, 7], k=13)",
        "candidate(nums=[0] * 100000, k=2147483647)",
        "candidate(nums=[1000000000, 1000000000, 147483647], k=2147483647)",
    }
    while len(calls) < 600:
        size = rng.randint(1, 100)
        values = [rng.randint(0, 1000) for _ in range(size)]
        k = rng.randint(1, _MAX_SUM)
        calls.add(f"candidate(nums={values!r}, k={k})")

    for call in calls:
        import ast

        node = ast.parse(call, mode="eval").body
        kwargs = {
            keyword.arg: eval(
                compile(ast.Expression(keyword.value), "<generated-argument>", "eval"),
                {"__builtins__": {}},
            )
            for keyword in node.keywords
        }
        values = kwargs["nums"]
        assert 1 <= len(values) <= _MAX_LENGTH
        assert all(0 <= value <= _MAX_VALUE for value in values)
        assert sum(values) <= _MAX_SUM
        assert 1 <= kwargs["k"] <= _MAX_SUM
    return sorted(calls)
