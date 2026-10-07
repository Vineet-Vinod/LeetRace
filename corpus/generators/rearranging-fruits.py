import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        a, b = kwargs["basket1"], kwargs["basket2"]
        assert 1 <= len(a) == len(b) <= 100000 and all(1 <= x <= 10**9 for x in a + b)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(basket1=[4, 2, 2, 2], basket2=[1, 4, 1, 2])
    add(basket1=[2, 3, 4, 1], basket2=[3, 2, 5, 1])
    add(basket1=[10**9] * 100000, basket2=[10**9] * 100000)
    add(basket1=[1, 1, 10**9, 10**9], basket2=[1, 1, 999999999, 999999999])
    add(basket1=[1], basket2=[2])
    while len(calls) < 600:
        n = rng.randint(1, 35)
        if len(calls) % 3:
            values = [rng.randint(1, 1000) for _ in range(n)]
            all_values = values * 2
            rng.shuffle(all_values)
            a, b = all_values[:n], all_values[n:]
        else:
            a = [rng.randint(1, 12) for _ in range(n)]
            b = [rng.randint(1, 12) for _ in range(n)]
        add(basket1=a, basket2=b)
    return calls
