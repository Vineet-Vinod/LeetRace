def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        n = rng.randint(1, 100)
        head = rng.randrange(n)
        order = [head] + [employee for employee in range(n) if employee != head]
        manager = [-1] * n
        children = [0] * n
        for index in range(1, n):
            employee = order[index]
            boss = rng.choice(order[:index])
            manager[employee] = boss
            children[boss] += 1
        inform = [rng.randint(0, 1000) if children[i] else 0 for i in range(n)]
        assert manager[head] == -1 and all(
            value == 0 or children[i] > 0 for i, value in enumerate(inform)
        )
        cases.add(
            f"candidate(n={n}, headID={head}, manager={manager!r}, informTime={inform!r})"
        )
    assert len(cases) >= 500
    return sorted(cases)[:600]
