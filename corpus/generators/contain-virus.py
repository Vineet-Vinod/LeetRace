import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        validate(kwargs)
        call = (
            "candidate(" + ", ".join(k + "=" + repr(v) for k, v in kwargs.items()) + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    def letters(text):
        return all("a" <= ch <= "z" for ch in text)

    def array(values, minimum, maximum, length):
        assert 1 <= len(values) <= length
        assert all(minimum <= v <= maximum for v in values)

    def no_ties(grid):
        # Independently simulate all threatened-cell sets on every day.
        active = {(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v}
        healthy = {
            (r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if not v
        }

        def neighbors(cell):
            r, c = cell
            return {(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)}

        while active and healthy:
            remaining = active.copy()
            groups = []
            while remaining:
                group = {remaining.pop()}
                todo = list(group)
                while todo:
                    linked = neighbors(todo.pop()) & remaining
                    remaining -= linked
                    group |= linked
                    todo.extend(linked)
                frontier = set().union(*(neighbors(cell) for cell in group)) & healthy
                groups.append((group, frontier))
            maximum = max(len(f) for _, f in groups)
            if maximum == 0:
                return True
            if sum(len(f) == maximum for _, f in groups) != 1:
                return False
            winner = next(g for g, f in groups if len(f) == maximum)
            spread = set().union(*(f for g, f in groups if g is not winner))
            active = (active - winner) | spread
            healthy -= spread
        return True

    def validate(d):
        g = d["isInfected"]
        assert 1 <= len(g) <= 50 and 1 <= len(g[0]) <= 50
        assert all(len(row) == len(g[0]) and set(row) <= {0, 1} for row in g)
        assert no_ties(g)

    add(isInfected=[[0]])
    add(isInfected=[[1]])
    add(isInfected=[[1] * 50 for _ in range(50)])
    add(isInfected=[[int(r == 25 and c == 25) for c in range(50)] for r in range(50)])
    add(isInfected=[[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    while len(calls) < 600:
        m, n = rng.randint(1, 10), rng.randint(1, 10)
        g = [
            [int(rng.random() < rng.choice([0.15, 0.35, 0.65, 0.85])) for _ in range(n)]
            for _ in range(m)
        ]
        if no_ties(g):
            add(isInfected=g)
    assert len(calls) == 600
    return calls
