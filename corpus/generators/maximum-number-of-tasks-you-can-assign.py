import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        t, w, p, s = (
            kwargs["tasks"],
            kwargs["workers"],
            kwargs["pills"],
            kwargs["strength"],
        )
        assert 1 <= len(t) <= 50000 and 1 <= len(w) <= 50000
        assert 0 <= p <= len(w) and 0 <= s <= 10**9
        assert all(0 <= x <= 10**9 for x in t + w)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(tasks=[3, 2, 1], workers=[0, 3, 3], pills=1, strength=1)
    add(tasks=[5, 4], workers=[0, 0, 0], pills=1, strength=5)
    add(tasks=[10, 15, 30], workers=[0, 10, 10, 10, 10], pills=3, strength=10)
    add(tasks=[10**9] * 50000, workers=[0] * 50000, pills=50000, strength=10**9)
    add(tasks=[10**9], workers=[0], pills=0, strength=10**9)
    add(tasks=[0], workers=[0], pills=0, strength=0)
    while len(calls) < 600:
        n, m = rng.randint(1, 25), rng.randint(1, 25)
        t = [rng.randint(0, 50) for _ in range(n)]
        w = [rng.randint(0, 50) for _ in range(m)]
        add(tasks=t, workers=w, pills=rng.randint(0, m), strength=rng.randint(0, 50))
    return calls
