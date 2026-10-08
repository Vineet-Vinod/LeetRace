import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        n = rng.randint(1, 50)
        order = list(range(n))
        rng.shuffle(order)
        rank = {person: i for i, person in enumerate(order)}
        richer = []
        for rich in range(n):
            for poor in range(n):
                if rank[rich] < rank[poor] and rng.random() < 0.05:
                    richer.append([rich, poor])
        quiet = list(range(n))
        rng.shuffle(quiet)
        key = (tuple(map(tuple, richer)), tuple(quiet))
        if key not in seen:
            seen.add(key)
            assert (
                len(quiet) == n
                and len(set(quiet)) == n
                and all(rank[a] < rank[b] for a, b in richer)
            )
            cases.append(f"candidate(richer={richer!r}, quiet={quiet!r})")
    return cases
