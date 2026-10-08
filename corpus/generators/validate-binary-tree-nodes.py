import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        (4, (1, -1, 3, -1), (2, -1, -1, -1)),
        (4, (1, -1, 3, -1), (2, 3, -1, -1)),
        (2, (1, 0), (-1, -1)),
    }
    while len(cases) < 600:
        n = rng.randint(1, 100)
        left = [-1] * n
        right = [-1] * n
        available = [0]
        for child in range(1, n):
            if not available:
                break
            parent = rng.choice(available)
            if left[parent] == -1 and right[parent] == -1:
                side = rng.choice((0, 1))
            else:
                side = 0 if left[parent] == -1 else 1
            if side == 0:
                left[parent] = child
            else:
                right[parent] = child
            if left[parent] != -1 and right[parent] != -1:
                available.remove(parent)
            available.append(child)
        if rng.random() < 0.2 and n > 1:
            left[rng.randrange(n)] = rng.randrange(n)
        cases.add((n, tuple(left), tuple(right)))
    return [
        f"candidate(n={n}, leftChild={list(left)!r}, rightChild={list(right)!r})"
        for n, left, right in cases
    ]
