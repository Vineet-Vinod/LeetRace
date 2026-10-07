def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 30)
        logs = []
        for i in range(n):
            ident = f"id{i}"
            if rng.random() < 0.5:
                content = " ".join(
                    rng.choice("abcdefghijklmnopqrstuvwxyz")
                    for _ in range(rng.randint(1, 4))
                )
            else:
                content = " ".join(
                    str(rng.randint(0, 999)) for _ in range(rng.randint(1, 4))
                )
            logs.append(f"{ident} {content}")
        cases.add(f"candidate(logs={logs!r})")
    return sorted(cases)
