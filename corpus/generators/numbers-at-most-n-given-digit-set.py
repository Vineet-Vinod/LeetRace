import random

EXAMPLES = [
    "candidate(digits=['1', '3', '5', '7'], n=100)",
    "candidate(digits=['1', '4', '9'], n=1000000000)",
    "candidate(digits=['7'], n=8)",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = list(EXAMPLES)
    seen = set(calls)

    def emit(call: str) -> None:
        if call not in seen:
            calls.append(call)
            seen.add(call)

    def add(digits, n):
        assert (
            1 <= len(digits) <= 9
            and digits == sorted(set(digits))
            and all(d in "123456789" and len(d) == 1 for d in digits)
        )
        assert 1 <= n <= 10**9
        emit(f"candidate(digits={digits!r}, n={n})")

    add(list("123456789"), 10**9)
    add(["9"], 1)
    add(["1"], 1)
    while len(calls) < 600:
        if rng.random() < 0.2:
            # Every permitted digit exceeds n, so no positive number qualifies.
            n = rng.randint(1, 8)
            available = [str(d) for d in range(n + 1, 10)]
            digits = sorted(rng.sample(available, rng.randint(1, len(available))))
        else:
            digits = sorted(rng.sample(list("123456789"), rng.randint(1, 9)))
            n = rng.choice(
                [
                    rng.randint(1, 1000),
                    rng.randint(1, 10**9),
                    int("".join(rng.choices(digits, k=rng.randint(1, 9)))),
                ]
            )
        add(digits, n)
    return calls
