import random


def successful_sequence(rng: random.Random, length: int) -> tuple[int, ...]:
    fives = 0
    tens = 0
    bills: list[int] = []
    for _ in range(length):
        valid = [5]
        if fives:
            valid.append(10)
        if tens and fives or fives >= 3:
            valid.append(20)
        bill = rng.choice(valid)
        bills.append(bill)
        if bill == 5:
            fives += 1
        elif bill == 10:
            fives -= 1
            tens += 1
        elif tens and fives:
            tens -= 1
            fives -= 1
        else:
            fives -= 3
    return tuple(bills)


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {
        (5,),
        (10,),
        (5, 5, 5, 10, 20),
        (5, 5, 10, 10, 20),
        (5,) * 100_000,
        (5,) * 99 + (20,),
    }
    while len(cases) < 600:
        cases.add(tuple(rng.choice((5, 10, 20)) for _ in range(rng.randint(1, 300))))
        cases.add(successful_sequence(rng, rng.randint(1, 300)))
    return [f"candidate(bills={list(bills)!r})" for bills in cases]
