import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def valid(s, t):
        if not (
            1 <= len(s) <= 1000
            and 1 <= len(t) <= 1000
            and all(
                c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                for c in s + t
            )
        ):
            return False
        # Independently enforce the promised 32-bit answer, rather than trusting golden output.
        counts = [1] + [0] * len(t)
        for c in s:
            for j in range(len(t) - 1, -1, -1):
                if c == t[j]:
                    counts[j + 1] += counts[j]
        return counts[-1] <= 2**31 - 1

    def emit(**args):
        assert valid(**args), args
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in args.items()) + ")"
        calls[call] = None

    for s, t in [
        ("rabbbit", "rabbit"),
        ("babgbag", "bag"),
        ("a" * 1000, "a" * 1000),
        ("a" * 1000, "b" * 1000),
        ("a" * 1000, "a"),
        ("A", "a"),
    ]:
        emit(s=s, t=t)
    while len(calls) < 600:
        s = "".join(rng.choice("abcABC") for _ in range(rng.randint(1, 18)))
        if rng.randrange(2):
            t = "".join(
                s[i] for i in sorted(rng.sample(range(len(s)), rng.randint(1, len(s))))
            )
        else:
            t = "".join(rng.choice("abcABCxyz") for _ in range(rng.randint(1, 20)))
        emit(s=s, t=t)
    assert len(calls) == 600
    return list(calls)
