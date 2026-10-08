import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        (("0.700", "2.800", "4.900"), 8),
        (("1.500", "2.500", "3.500"), 10),
        (("1.500", "2.500", "3.500"), 9),
    }
    while len(cases) < 600:
        prices = tuple(
            f"{amount // 1000}.{amount % 1000:03d}"
            for amount in (rng.randint(0, 1_000_000) for _ in range(rng.randint(1, 40)))
        )
        target = rng.randint(
            0,
            min(
                10**6,
                sum(int(p.split(".")[0]) + (int(p.split(".")[1]) > 0) for p in prices),
            ),
        )
        cases.add((prices, target))
    return [
        f"candidate(prices={list(prices)!r}, target={target})"
        for prices, target in cases
    ]
