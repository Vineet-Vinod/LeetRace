import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(blocked: list[list[int]], source: list[int], target: list[int]) -> None:
        assert 0 <= len(blocked) <= 200 and len({tuple(x) for x in blocked}) == len(
            blocked
        )
        assert all(
            len(c) == 2 and all(0 <= v < 1000000 for v in c)
            for c in blocked + [source, target]
        )
        assert source != target and source not in blocked and target not in blocked
        call = (
            "candidate("
            + ", ".join(
                f"{key}={value!r}"
                for key, value in [
                    ("blocked", blocked),
                    ("source", source),
                    ("target", target),
                ]
            )
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(blocked=[[0, 1], [1, 0]], source=[0, 0], target=[0, 2])
    add(blocked=[], source=[0, 0], target=[999999, 999999])
    add(
        blocked=[[i, 199 - i] for i in range(200)],
        source=[0, 0],
        target=[999999, 999999],
    )
    add(
        blocked=[[i, 199 - i] for i in range(200)],
        source=[500000, 500000],
        target=[999999, 999999],
    )
    add(blocked=[[0, 1], [1, 0]], source=[0, 0], target=[0, 2])
    add(blocked=[], source=[0, 0], target=[999999, 999999])
    while len(calls) < 600:
        x, y = rng.randint(1, 999997), rng.randint(1, 999997)
        source = [x, y]
        target = [rng.randrange(1000000), rng.randrange(1000000)]
        if target == source:
            continue
        if len(calls) % 2 == 0:
            blocked = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]
        else:
            blocked = [
                list(c)
                for c in {
                    (rng.randrange(1000000), rng.randrange(1000000))
                    for _ in range(rng.randint(0, 15))
                }
                if list(c) not in [source, target]
            ]
        if target in blocked:
            continue
        add(blocked=blocked, source=source, target=target)
    return calls
