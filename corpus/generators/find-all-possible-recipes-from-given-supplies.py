def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(recipes=['bread'],ingredients=[['yeast','flour']],supplies=['yeast','flour','corn'])",
        "candidate(recipes=['bread','sandwich'],ingredients=[['yeast','flour'],['bread','meat']],supplies=['yeast','flour','meat'])",
        "candidate(recipes=['bread','sandwich','burger'],ingredients=[['yeast','flour'],['bread','meat'],['sandwich','meat','bread']],supplies=['yeast','flour','meat'])",
    }
    for n in range(1, 7):
        recipes = [f"r{i}" for i in range(n)]
        ingredients = [["base"] if i == 0 else [f"r{i - 1}"] for i in range(n)]
        supplies = ["base"]
        cases.add(
            f"candidate(recipes={recipes!r},ingredients={ingredients!r},supplies={supplies!r})"
        )
    while len(cases) < 600:
        n = rng.randint(1, 12)
        recipes = [f"r{i}" for i in range(n)]
        ingredients = []
        for i in range(n):
            options = ["base"] + [f"r{j}" for j in range(n) if j != i]
            ingredients.append(
                rng.sample(options, rng.randint(1, min(4, len(options))))
            )
        supplies = rng.sample(["base", "salt", "water", "flour"], rng.randint(1, 4))
        cases.add(
            f"candidate(recipes={recipes!r},ingredients={ingredients!r},supplies={supplies!r})"
        )
    return sorted(cases)
