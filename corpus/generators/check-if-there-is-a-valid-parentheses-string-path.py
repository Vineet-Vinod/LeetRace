import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        g = kw["grid"]
        m, n = len(g), len(g[0])
        assert 1 <= m <= 100 and 1 <= n <= 100
        assert all(len(row) == n and set(row) <= set("()") for row in g)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kw.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for kw in [
        {"grid": [["(", "(", "("], [")", "(", ")"], ["(", "(", ")"], ["(", "(", ")"]]},
        {"grid": [[")", ")"], ["(", "("]]},
    ] + [
        {"grid": [["("] * 100 for _ in range(99)]},
        {"grid": [["(" if i + j < 99 else ")" for j in range(100)] for i in range(99)]},
        {"grid": [[")"] * 100 for _ in range(100)]},
    ]:
        add(**kw)
    while len(calls) < 600:
        m, n = rng.randint(1, 12), rng.randint(1, 12)
        g = [[rng.choice("()") for _ in range(n)] for _ in range(m)]
        if len(calls) % 2 == 0:
            if (m + n) % 2 == 0:
                n += 1
                g = [row + [rng.choice("()")] for row in g]
            # Construct a valid path along the top edge then down the right edge.
            path = "(" * ((m + n - 1) // 2) + ")" * ((m + n - 1) // 2)
            for j in range(n):
                g[0][j] = path[j]
            for i in range(1, m):
                g[i][-1] = path[n + i - 1]
        add(grid=g)
    return calls
