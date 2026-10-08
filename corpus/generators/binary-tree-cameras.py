import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = dict.fromkeys(
        ast.unparse(ast.parse(call, mode="eval"))
        for call in [
            "candidate(root=tree_node([0,0,None,0,0]))",
            "candidate(root=tree_node([0,0,None,0,None,0,None,None,0]))",
        ]
    )

    def add(data):
        assert 1 <= sum(x is not None for x in data) <= 1000
        assert data[0] == 0 and all(x is None or x == 0 for x in data)
        slots = 1
        for x in data:
            assert slots > 0
            slots -= 1
            if x is not None:
                slots += 2
        calls[
            ast.unparse(ast.parse(f"candidate(root=tree_node({data!r}))", mode="eval"))
        ] = None

    add([0])
    add([0] * 1000)
    add([0, None] * 999 + [0])
    while len(calls) < 600:
        n = rng.randint(1, 100)
        children = [[None, None] for _ in range(n)]
        available = [(0, 0), (0, 1)]
        for i in range(1, n):
            index = rng.randrange(len(available))
            parent, side = available.pop(index)
            children[parent][side] = i
            available.extend([(i, 0), (i, 1)])
        queue = [0]
        data = []
        for i in queue:
            if i is None:
                data.append(None)
            else:
                data.append(0)
                queue.extend(children[i])
        while data[-1] is None:
            data.pop()
        add(data)
    return list(calls)
