import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**args) -> None:
        a = args["slices"]
        assert 1 <= len(a) <= 500 and len(a) % 3 == 0 and all(1 <= v <= 1000 for v in a)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in args.items())
            + ")"
        )
        calls[call] = None

    add(slices=[1, 2, 3, 4, 5, 6])
    add(slices=[8, 9, 8, 6, 1, 1])
    # 498 is the largest feasible length under the multiple-of-three promise.
    add(slices=[1000] * 498)
    add(slices=[1, 1000, 1] * 166)
    add(slices=[1, 2, 3, 4, 5, 6])
    add(slices=[8, 9, 8, 6, 1, 1])
    while len(calls) < 600:
        a = [rng.randint(1, 1000) for _ in range(3 * rng.randint(1, 15))]
        if len(calls) % 3 == 0:
            a.sort()
        if len(calls) % 3 == 1:
            a.sort(reverse=True)
        add(slices=a)
    return list(calls)[:600]
