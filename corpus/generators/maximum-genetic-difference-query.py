import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        def render(value):
            # Repeat only immutable scalar values; nested input lists retain distinct identities.
            if isinstance(value, list):
                if (
                    len(value) >= 1000
                    and isinstance(value[0], (int, str))
                    and all(x == value[0] for x in value)
                ):
                    return f"[{value[0]!r}] * {len(value)}"
                return "[" + ", ".join(render(x) for x in value) + "]"
            return repr(value)

        call = (
            "candidate("
            + ", ".join(f"{key}={render(value)}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    def case(parents, queries):
        n = len(parents)
        assert 2 <= n <= 100000 and parents.count(-1) == 1
        # Check rooted-tree validity independently of the golden using root traversal.
        children = [[] for _ in parents]
        for i, p in enumerate(parents):
            if p != -1:
                assert 0 <= p < n and p != i
                children[p].append(i)
        reached = [parents.index(-1)]
        for node in reached:
            reached.extend(children[node])
        assert len(reached) == n and len(set(reached)) == n
        assert 1 <= len(queries) <= 30000 and all(
            0 <= u < n and 0 <= v <= 200000 for u, v in queries
        )
        add(parents=parents, queries=queries)

    case([-1, 0, 1, 1], [[0, 2], [3, 2], [2, 5]])
    case([-1] + list(range(99999)), [[99999, 200000], [0, 0]])
    case([-1] + [0] * 99999, [[i, 200000 if i % 2 else 0] for i in range(30000)])
    case([3, 7, -1, 2, 0, 7, 0, 2], [[4, 6], [1, 15], [0, 5]])
    while len(calls) < 600:
        n = rng.randint(2, 65)
        order = rng.sample(range(n), n)
        p = [-1] * n
        for j in range(1, n):
            p[order[j]] = order[rng.randrange(j)]
        case(
            p,
            [
                [rng.randrange(n), rng.randint(0, 200000)]
                for _ in range(rng.randint(1, 40))
            ],
        )
    assert len(calls) == 600
    return calls
