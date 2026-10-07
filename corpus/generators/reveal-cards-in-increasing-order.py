import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {
        (17, 13, 11, 2, 3, 5, 7),
        (1, 1000),
        (1,),
        (1000,),
        (1_000_000,),
    }
    cases.add(tuple(range(1, 1001)))
    while len(cases) < 600:
        size = rng.randint(1, 80)
        cases.add(tuple(rng.sample(range(1, 1_000_001), size)))
    assert all(
        1 <= len(deck) <= 1000
        and len(set(deck)) == len(deck)
        and all(1 <= card <= 1_000_000 for card in deck)
        for deck in cases
    )
    return [f"candidate(deck={list(deck)!r})" for deck in sorted(cases)]
