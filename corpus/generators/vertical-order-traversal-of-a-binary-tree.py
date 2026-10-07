import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(root: list[int | None]) -> None:
        assert 1 <= sum(x is not None for x in root) <= 1000
        assert root[0] is not None and all(x is None or 0 <= x <= 1000 for x in root)
        slots = 1
        for x in root:
            assert slots > 0
            slots -= 1
            if x is not None:
                slots += 2
        call = "candidate(root=tree_node(" + repr(root) + "))"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(root=[3, 9, 20, None, None, 15, 7])
    add(root=[1, 2, 3, 4, 6, 5, 7])
    add(root=list(range(1000)))
    add(root=[1000] + [v for i in range(999) for v in [None, i]])
    add(root=[3, 9, 20, None, None, 15, 7])
    add(root=[1, 2, 3, 4, 5, 6, 7])
    add(root=[1, 2, 3, 4, 6, 5, 7])
    while len(calls) < 600:
        n = rng.randint(1, 45)
        root = [rng.randint(0, 1000)]
        remaining = n - 1
        pending = 1
        while remaining:
            pending -= 1
            for child in range(2):
                if remaining and (pending == 0 or rng.random() < 0.7):
                    root.append(rng.randint(0, 1000))
                    remaining -= 1
                    pending += 1
                else:
                    root.append(None)
        while root[-1] is None:
            root.pop()
        add(root=root)
    return calls
