def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 100)
        values = [0] * n
        next_value = 0

        def assign(index: int) -> None:
            nonlocal next_value
            if index >= n:
                return
            assign(2 * index + 1)
            values[index] = next_value
            next_value += 1
            assign(2 * index + 2)

        assign(0)
        k = rng.randint(1, n)
        cases.add(f"candidate(root=tree_node({values!r}),k={k})")
    return sorted(cases)
