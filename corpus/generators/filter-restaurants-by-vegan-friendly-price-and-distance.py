def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            "candidate(restaurants=[[1, 4, 1, 40, 10], [2, 8, 0, 50, 5]], veganFriendly=1, maxPrice=50, maxDistance=10)",
            "candidate(restaurants=[[i + 1, 1 + i % 100, i % 2, i + 1, i + 1] for i in range(10000)], veganFriendly=0, maxPrice=10000, maxDistance=10000)",
            "candidate(restaurants=[[1, 100000, 1, 100000, 100000]], veganFriendly=0, maxPrice=100000, maxDistance=100000)",
            "candidate(restaurants=[[100000, 100000, 1, 100000, 100000]], veganFriendly=1, maxPrice=100000, maxDistance=100000)",
        ]
    )
    for index in range(600):
        size = 1 + index % 100
        ids = rng.sample(range(1, 100001), size)
        restaurants = [
            [
                ids[j],
                rng.randint(1, 100),
                rng.randrange(2),
                rng.randint(1, 100000),
                rng.randint(1, 100000),
            ]
            for j in range(size)
        ]
        vegan, price, distance = (
            rng.randrange(2),
            rng.randint(1, 100000),
            rng.randint(1, 100000),
        )
        cases.add(
            f"candidate(restaurants={restaurants!r}, veganFriendly={vegan}, maxPrice={price}, maxDistance={distance})"
        )
    return sorted(cases)
