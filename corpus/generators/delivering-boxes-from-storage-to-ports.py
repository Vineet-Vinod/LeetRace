import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(
        boxes: list[list[int]], portsCount: int, maxBoxes: int, maxWeight: int
    ) -> None:
        assert (
            1 <= len(boxes) <= 100000
            and 1 <= portsCount <= 100000
            and 1 <= maxBoxes <= 100000
            and 1 <= maxWeight <= 100000
        )
        assert all(
            len(b) == 2 and 1 <= b[0] <= portsCount and 1 <= b[1] <= maxWeight
            for b in boxes
        )
        call = (
            "candidate("
            + ", ".join(
                f"{key}={value!r}"
                for key, value in [
                    ("boxes", boxes),
                    ("portsCount", portsCount),
                    ("maxBoxes", maxBoxes),
                    ("maxWeight", maxWeight),
                ]
            )
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(boxes=[[1, 1], [2, 1], [1, 1]], portsCount=2, maxBoxes=3, maxWeight=3)
    add(
        boxes=[[i % 100000 + 1, 1] for i in range(100000)],
        portsCount=100000,
        maxBoxes=100000,
        maxWeight=100000,
    )
    add(boxes=[[100000, 100000]], portsCount=100000, maxBoxes=1, maxWeight=100000)
    add(boxes=[[1, 1], [2, 1], [1, 1]], portsCount=2, maxBoxes=3, maxWeight=3)
    add(
        boxes=[[1, 2], [3, 3], [3, 1], [3, 1], [2, 4]],
        portsCount=3,
        maxBoxes=3,
        maxWeight=6,
    )
    add(
        boxes=[[1, 4], [1, 2], [2, 1], [2, 1], [3, 2], [3, 4]],
        portsCount=3,
        maxBoxes=6,
        maxWeight=7,
    )
    while len(calls) < 600:
        n = rng.randint(1, 40)
        p = rng.randint(1, 8)
        w = rng.randint(1, 40)
        boxes = [[rng.randint(1, p), rng.randint(1, w)] for _ in range(n)]
        if len(calls) % 3 == 0:
            boxes = [[1, rng.randint(1, w)] for _ in range(n)]
        add(boxes=boxes, portsCount=p, maxBoxes=rng.randint(1, n + 5), maxWeight=w)
    return calls
