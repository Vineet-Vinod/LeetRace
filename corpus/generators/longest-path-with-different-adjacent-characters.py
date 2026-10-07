import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**args) -> None:
        p, s = args["parent"], args["s"]
        n = len(p)
        assert (
            1 <= n <= 100000
            and len(s) == n
            and set(s) <= set("abcdefghijklmnopqrstuvwxyz")
            and p[0] == -1
        )
        assert all(0 <= x < n for x in p[1:])
        # Explicit reachability proves a tree, including relabelings with parent[i]>i.
        children = [[] for _ in p]
        for i in range(1, n):
            children[p[i]].append(i)
        stack = [0]
        visited = set()
        while stack:
            node = stack.pop()
            assert node not in visited
            visited.add(node)
            stack.extend(children[node])
        assert len(visited) == n
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in args.items())
            + ")"
        )
        calls[call] = None

    add(parent=[-1, 0, 0, 1, 1, 2], s="abacbe")
    add(parent=[-1, 0, 0, 0], s="aabc")
    add(parent=[-1] + list(range(99999)), s="ab" * 50000)
    add(parent=[-1] + [0] * 99999, s="a" * 100000)
    add(parent=[-1, 0, 0, 1, 1, 2], s="abacbe")
    while len(calls) < 600:
        n = rng.randint(1, 65)
        p = [-1] + [rng.randrange(i) for i in range(1, n)]
        s = "".join(rng.choices("abc", k=n))
        if len(calls) % 4 == 0:
            s = "a" * n
        if len(calls) % 4 == 1:
            permutation = [0] + rng.sample(list(range(1, n)), n - 1)
            new_p = [-1] * n
            new_s = [""] * n
            for i in range(n):
                new_s[permutation[i]] = s[i]
                if i:
                    new_p[permutation[i]] = permutation[p[i]]
            p, s = new_p, "".join(new_s)
        add(parent=p, s=s)
    return list(calls)[:600]
