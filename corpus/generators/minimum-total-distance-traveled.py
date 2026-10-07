import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def valid(robot, factory):
        return (
            1 <= len(robot) <= 100
            and 1 <= len(factory) <= 100
            and len(set(robot)) == len(robot)
            and len({p for p, c in factory}) == len(factory)
            and all(-(10**9) <= p <= 10**9 for p in robot)
            and all(-(10**9) <= p <= 10**9 and 0 <= c <= len(robot) for p, c in factory)
            and sum(c for p, c in factory) >= len(robot)
        )

    def emit(**args):
        assert valid(**args), args
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in args.items()) + ")"
        calls[call] = None

    emit(robot=[0, 4, 6], factory=[[2, 2], [6, 2]])
    emit(robot=[1, -1], factory=[[-2, 1], [2, 1]])
    emit(
        robot=list(range(-(10**9), -(10**9) + 100)),
        factory=[[10**9 - i, 100] for i in range(100)],
    )
    emit(robot=list(range(100)), factory=[[i, 1] for i in range(100)])
    while len(calls) < 600:
        n = rng.randint(1, 15)
        m = rng.randint(1, 15)
        robot = rng.sample(range(-100, 101), n)
        positions = rng.sample(range(-100, 101), m)
        capacities = [rng.randint(0, n) for _ in range(m)]
        if sum(capacities) < n:
            capacities[0] = n
        factory = [[p, c] for p, c in zip(positions, capacities)]
        if rng.randrange(5) == 0:
            factory = [[p, 1] for p in robot]
        emit(robot=robot, factory=factory)
    assert len(calls) == 600
    return list(calls)
