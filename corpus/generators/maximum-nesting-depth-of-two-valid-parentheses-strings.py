def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        pairs = rng.randint(1, 100)
        depth = 0
        seq = []
        for i in range(2 * pairs):
            if depth == 0 or (i < 2 * pairs - 1 and rng.random() < 0.55):
                seq.append("(")
                depth += 1
            else:
                seq.append(")")
                depth -= 1
        seq.extend(")" * depth)
        cases.add(f"candidate(seq={''.join(seq)!r})")
    return sorted(cases)
