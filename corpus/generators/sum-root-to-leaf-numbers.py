import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set()
    while len(cases) < 600:
        size = 1 + rng.randrange(100)
        values = [rng.randrange(10) for _ in range(size)]
        cases.add(f"candidate(root=tree_node({values!r}))")
    cases.add(f"candidate(root=tree_node({[0] * 1000!r}))")
    boundary = [0] * 1000
    boundary[-1] = 1
    cases.add(f"candidate(root=tree_node({boundary!r}))")
    return sorted(cases)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(root=tree_node([1, 2, 3]))",
    "candidate(root=tree_node([4, 9, 0, 5, 1]))",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
