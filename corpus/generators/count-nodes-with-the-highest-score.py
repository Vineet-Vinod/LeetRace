import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {(-1, 2, 0, 2, 0), (-1, 2, 0)}
    while len(cases) < 600:
        n = rng.randint(2, 100)
        parents = [-1]
        children = [0] * n
        for node in range(1, n):
            eligible = [p for p in range(node) if children[p] < 2]
            parent = rng.choice(eligible)
            parents.append(parent)
            children[parent] += 1
        cases.add(tuple(parents))
    return [f"candidate(parents={list(parents)!r})" for parents in cases]
