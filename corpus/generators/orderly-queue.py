import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(s: str, k: int) -> None:
        assert 1 <= k <= len(s) <= 1000 and all("a" <= c <= "z" for c in s)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in [("s", s), ("k", k)])
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(s="cba", k=1)
    add(s="baaca", k=3)
    add(s="zyxwvutsrqponmlkjihgfedcba" * 38 + "zyxwvutsrqpo", k=1)
    add(s="z" * 1000, k=1000)
    add(s="cba", k=1)
    add(s="baaca", k=3)
    while len(calls) < 600:
        s = "".join(rng.choices("abcdef", k=rng.randint(1, 80)))
        add(s=s, k=rng.choice([1, len(s), rng.randint(1, len(s))]))
    return calls
