def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        ["candidate(head=list_node([18, 6, 10, 3]))", "candidate(head=list_node([7]))"]
    )
    for index in range(600):
        size = 1 + index % 100
        if index == 0:
            size = 5000
        values = [rng.randint(1, 1000) for _ in range(size)]
        cases.add(f"candidate(head=list_node({values!r}))")
    return sorted(cases)
