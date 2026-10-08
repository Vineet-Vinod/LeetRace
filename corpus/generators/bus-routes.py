import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(routes: list[list[int]], source: int, target: int) -> None:
        assert 1 <= len(routes) <= 500 and sum(map(len, routes)) <= 100000
        assert all(
            1 <= len(route) <= 100000
            and len(set(route)) == len(route)
            and all(0 <= x < 1000000 for x in route)
            for route in routes
        )
        assert 0 <= source < 1000000 and 0 <= target < 1000000
        call = (
            "candidate("
            + ", ".join(
                f"{key}={value!r}"
                for key, value in [
                    ("routes", routes),
                    ("source", source),
                    ("target", target),
                ]
            )
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(routes=[[1, 2, 7], [3, 6, 7]], source=1, target=6)
    add(routes=[list(range(100000))], source=0, target=99999)
    add(routes=[[i, i + 1] for i in range(500)], source=0, target=500)
    add(routes=[[999999]], source=0, target=0)
    add(routes=[[1, 2, 7], [3, 6, 7]], source=1, target=6)
    add(routes=[[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], source=15, target=12)
    while len(calls) < 600:
        n = rng.randint(1, 15)
        if len(calls) % 3 == 0:
            routes = [[i, i + 1, rng.randrange(20, 50)] for i in range(n)]
            source, target = 0, n
        else:
            routes = [rng.sample(range(50), rng.randint(1, 12)) for _ in range(n)]
            source, target = rng.randrange(55), rng.randrange(55)
        add(routes=routes, source=source, target=target)
    return calls
