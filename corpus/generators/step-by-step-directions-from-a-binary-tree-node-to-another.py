import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(2, 100)
        start, dest = rng.sample(range(1, n + 1), 2)
        cases.add((n, start, dest))
    calls = [
        f"candidate(root=tree_node({list(range(1, n + 1))!r}), startValue={start}, destValue={dest})"
        for n, start, dest in cases
    ]
    calls.append(
        f"candidate(root=tree_node({list(range(1, 100001))!r}), startValue=1, destValue=100000)"
    )
    assert 500 <= len(calls) <= 999
    assert len(calls) == len(set(calls))
    return calls
