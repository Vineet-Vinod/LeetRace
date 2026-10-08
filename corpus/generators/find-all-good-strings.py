import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def valid(n, s1, s2, evil):
        return (
            1 <= n <= 500
            and len(s1) == len(s2) == n
            and s1 <= s2
            and 1 <= len(evil) <= 50
            and all("a" <= c <= "z" for c in s1 + s2 + evil)
        )

    def emit(**args):
        assert valid(**args), args
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in args.items()) + ")"
        calls[call] = None

    emit(n=2, s1="aa", s2="da", evil="b")
    emit(n=8, s1="leetcode", s2="leetgoes", evil="leet")
    emit(n=500, s1="a" * 500, s2="z" * 500, evil="ab" * 25)
    emit(n=500, s1="a" * 500, s2="a" * 500, evil="a")
    while len(calls) < 600:
        n = rng.randint(1, 10)
        prefix = "".join(rng.choice("abcxyz") for _ in range(max(0, n - 2)))
        s1 = prefix + "".join(
            rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(n - len(prefix))
        )
        s2 = prefix + "".join(
            rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(n - len(prefix))
        )
        s1, s2 = sorted([s1, s2])
        evil = rng.choice(
            [
                prefix if prefix else "a",
                "".join(rng.choice("abcxyz") for _ in range(rng.randint(1, 8))),
            ]
        )
        emit(n=n, s1=s1, s2=s2, evil=evil)
    assert len(calls) == 600
    return list(calls)
