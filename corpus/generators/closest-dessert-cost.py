def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(baseCosts=[1, 7], toppingCosts=[3, 4], target=10)"])
    for index in range(600):
        n, m = 1 + index % 10, 1 + (index * 7) % 10
        base = [rng.randint(1, 10000) for _ in range(n)]
        toppings = [rng.randint(1, 10000) for _ in range(m)]
        target = rng.randint(1, 10000)
        cases.add(
            f"candidate(baseCosts={base!r}, toppingCosts={toppings!r}, target={target})"
        )
    while len(cases) < 600:
        base = [rng.randint(1, 10000) for _ in range(rng.randint(1, 10))]
        toppings = [rng.randint(1, 10000) for _ in range(rng.randint(1, 10))]
        cases.add(
            f"candidate(baseCosts={base!r}, toppingCosts={toppings!r}, target={rng.randint(1, 10000)})"
        )
    return sorted(cases)
