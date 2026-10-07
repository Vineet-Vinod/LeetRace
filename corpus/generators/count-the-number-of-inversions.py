import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        n, req = kwargs["n"], kwargs["requirements"]
        assert 2 <= n <= 300 and 1 <= len(req) <= n
        assert len({e for e, c in req}) == len(req) and any(e == n - 1 for e, c in req)
        assert all(0 <= e < n and 0 <= c <= 400 for e, c in req)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(n=300, requirements=[[299, 400]])
    add(n=300, requirements=[[i, 0] for i in range(300)])
    add(n=3, requirements=[[2, 2], [0, 0]])
    add(n=3, requirements=[[2, 2], [1, 1], [0, 0]])
    add(n=2, requirements=[[0, 0], [1, 0]])
    while len(calls) < 600:
        n = rng.randint(2, 20)
        ends = sorted(set([n - 1] + rng.sample(range(n), rng.randrange(n))))
        if len(calls) % 2:
            perm = list(range(n))
            rng.shuffle(perm)
            requirements = [
                [
                    e,
                    sum(
                        perm[a] > perm[b]
                        for a in range(e + 1)
                        for b in range(a + 1, e + 1)
                    ),
                ]
                for e in ends
            ]
        else:
            requirements = [
                [e, rng.randint(0, min(400, n * (n - 1) // 2 + 5))] for e in ends
            ]
        add(n=n, requirements=requirements)
    return calls
