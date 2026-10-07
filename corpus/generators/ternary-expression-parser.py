def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(expression='T?2:3')",
        "candidate(expression='F?1:T?4:5')",
        "candidate(expression='T?T?F:5:3')",
    }

    def build(depth: int) -> str:
        if depth == 0 or rng.random() < 0.35:
            return rng.choice("0123456789TF")
        return rng.choice("TF") + "?" + build(depth - 1) + ":" + build(depth - 1)

    while len(cases) < 600:
        expr = build(3)
        if len(expr) >= 5:
            cases.add(f"candidate(expression={expr!r})")
    return sorted(cases)
