def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(s='3+2*2')", "candidate(s=' 3/2 ')"}
    while len(cases) < 600:
        count = rng.randint(1, 18)
        terms = [str(rng.randint(0, 3))]
        for _ in range(count - 1):
            operator = rng.choice("+-*/")
            value = rng.randint(1, 3) if operator == "/" else rng.randint(0, 3)
            terms.extend([operator, str(value)])
        expression = " ".join(terms)
        cases.add(f"candidate(s={expression!r})")
    return sorted(cases)
