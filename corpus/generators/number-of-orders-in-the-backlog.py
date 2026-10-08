import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, int, int], ...]] = {
        ((10, 5, 0), (15, 2, 1), (25, 1, 1), (30, 4, 0)),
        ((7, 1_000_000_000, 1), (15, 3, 0), (5, 999_999_995, 0), (5, 1, 1)),
        ((100, 8, 0), (99, 3, 1), (100, 4, 0), (100, 3, 1)),
        ((1_000_000_000, 1_000_000_000, 0), (1_000_000_000, 1_000_000_000, 1)),
        tuple((100, 100_000, direction) for direction in (0, 1) for _ in range(5_000)),
    }
    while len(cases) < 600:
        size = rng.randint(1, 100)
        if rng.random() < 0.6:
            price = rng.randint(1, 1000)
            orders = tuple(
                (price, rng.randint(1, 10**6), rng.randint(0, 1)) for _ in range(size)
            )
        else:
            orders = tuple(
                (rng.randint(1, 10**9), rng.randint(1, 10**9), rng.randint(0, 1))
                for _ in range(size)
            )
        cases.add(orders)
    assert all(
        1 <= len(orders) <= 100_000
        and all(
            1 <= price <= 10**9 and 1 <= amount <= 10**9 and order_type in (0, 1)
            for price, amount, order_type in orders
        )
        for orders in cases
    )
    return [
        f"candidate(orders={[list(order) for order in orders]!r})"
        for orders in sorted(cases)
    ]
