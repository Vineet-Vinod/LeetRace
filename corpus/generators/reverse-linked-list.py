def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    arrays = {
        (),
        (1,),
        (1, 2),
        (1, 2, 3, 4, 5),
        tuple((i % 10001) - 5000 for i in range(5000)),
    }
    while len(arrays) < 600:
        arrays.add(tuple(rng.randint(-5000, 5000) for _ in range(rng.randint(0, 100))))
    return [f"candidate(head=list_node({list(a)!r}))" for a in sorted(arrays)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(head=list_node([1, 2, 3, 4, 5]))",
    "candidate(head=list_node([1, 2]))",
    "candidate(head=list_node([]))",
]
_ORIGINAL_GENERATE = generate


def generate(seed: int = 0) -> list[str]:
    import ast

    calls = _ORIGINAL_GENERATE(seed) + _STATEMENT_EXAMPLE_CALLS
    unique = {}
    for call in calls:
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        unique.setdefault(key, call)
    return [unique[key] for key in sorted(unique)]
