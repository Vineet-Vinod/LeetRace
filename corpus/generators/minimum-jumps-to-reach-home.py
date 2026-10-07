def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(forbidden=[14, 4, 18, 1, 15], a=3, b=15, x=9)",
        "candidate(forbidden=list(range(1, 1001)), a=2000, b=2000, x=1001)",
        "candidate(forbidden=[2000], a=2000, b=2000, x=0)",
    }

    def validate(forbidden: list[int], a: int, b: int, x: int) -> None:
        assert 1 <= len(forbidden) <= 1000
        assert 1 <= a <= 2000 and 1 <= b <= 2000 and 0 <= x <= 2000
        assert len(forbidden) == len(set(forbidden))
        assert all(1 <= position <= 2000 for position in forbidden)
        assert x not in forbidden

    def add(forbidden: list[int], a: int, b: int, x: int) -> None:
        validate(forbidden, a, b, x)
        cases.add(f"candidate(forbidden={forbidden!r}, a={a}, b={b}, x={x})")

    while len(cases) < 600:
        a, b = rng.randint(1, 2000), rng.randint(1, 2000)
        x = rng.randint(0, 2000)
        positions = rng.sample(range(1, 2001), rng.randint(1, 80))
        forbidden = [position for position in positions if position != x]
        if not forbidden:
            forbidden = [1 if x != 1 else 2]
        add(forbidden, a, b, x)
    for call in cases:
        eval(call, {"candidate": validate})
    return sorted(cases)
