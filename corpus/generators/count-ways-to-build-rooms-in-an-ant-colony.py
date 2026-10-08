import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def valid(prevRoom):
        n = len(prevRoom)
        if not (
            2 <= n <= 100000
            and prevRoom[0] == -1
            and all(0 <= p < n for p in prevRoom[1:])
        ):
            return False
        children = [[] for _ in prevRoom]
        for i in range(1, n):
            children[prevRoom[i]].append(i)
        seen = {0}
        todo = [0]
        for u in todo:
            for v in children[u]:
                if v in seen:
                    return False
                seen.add(v)
                todo.append(v)
        return len(seen) == n

    def emit(**args):
        assert valid(**args), args
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in args.items()) + ")"
        calls[call] = None

    for p in [
        [-1, 0, 1],
        [-1, 0, 0, 1, 2],
        [-1] + list(range(99999)),
        [-1] + [0] * 99999,
    ]:
        emit(prevRoom=p)
    while len(calls) < 600:
        n = rng.randint(2, 60)
        parents = [-1] + [rng.randrange(i) for i in range(1, n)]
        labels = [0] + rng.sample(list(range(1, n)), n - 1)
        result = [-1] * n
        for i in range(1, n):
            result[labels[i]] = labels[parents[i]]
        emit(prevRoom=result)
    assert len(calls) == 600
    return list(calls)
