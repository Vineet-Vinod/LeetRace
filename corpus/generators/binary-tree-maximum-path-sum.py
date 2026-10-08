import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        v = kwargs["root"]
        assert 1 <= sum(x is not None for x in v) <= 30000
        assert v[0] is not None and all(x is None or -1000 <= x <= 1000 for x in v)
        slots = 1
        for x in v:
            assert slots > 0
            slots -= 1
            if x is not None:
                slots += 2
        call = f"candidate(root=tree_node({kwargs['root']!r}))"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(root=[1, 2, 3])
    add(root=[-10, 9, 20, None, None, 15, 7])
    add(root=[1000] * 30000)
    add(root=[-1000] * 30000)
    add(root=[1000] + [x for _ in range(29999) for x in (None, 1000)])
    add(root=[-1000])
    add(root=[0])
    while len(calls) < 600:
        n = rng.randint(1, 60)
        v = [rng.randint(-1000, 1000)]
        slots = 2
        count = 1
        while count < n:
            if slots > 1 and rng.random() < 0.3:
                v.append(None)
                slots -= 1
            else:
                v.append(rng.randint(-40, 40))
                slots += 1
                count += 1
        add(root=v)
    return calls
