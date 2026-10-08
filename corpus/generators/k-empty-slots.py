import random
from itertools import permutations


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        calls[
            "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        ] = None

    add(bulbs=list(range(1, 20001)), k=20000)
    add(bulbs=[1, 20000] + list(range(2, 20000)), k=19998)
    for n in range(1, 6):
        for p in permutations(range(1, n + 1)):
            for k in range(n + 1):
                if len(calls) < 350:
                    add(bulbs=list(p), k=k)
    while len(calls) < 600:
        n = rng.randint(2, 70)
        bulbs = list(range(1, n + 1))
        rng.shuffle(bulbs)
        k = rng.randint(0, n + 3)
        assert sorted(bulbs) == list(range(1, n + 1)) and 0 <= k <= 20000
        add(bulbs=bulbs, k=k)
    assert len(calls) == 600
    return list(calls)
