import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**args) -> None:
        assert all(
            1 <= len(args[s]) <= 100
            and set(args[s]) <= set("abcdefghijklmnopqrstuvwxyz")
            for s in ("s1", "s2")
        )
        assert 1 <= args["n1"] <= 10**6 and 1 <= args["n2"] <= 10**6
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in args.items())
            + ")"
        )
        calls[call] = None

    add(s1="acb", n1=4, s2="ab", n2=2)
    add(s1="acb", n1=1, s2="acb", n2=1)
    add(s1="acb", n1=4, s2="ab", n2=2)
    add(s1="a" * 100, n1=10**6, s2="a" * 100, n2=10**6)
    add(s1="ab" * 50, n1=10**6, s2="ba" * 50, n2=1)
    add(s1="a", n1=1, s2="z" * 100, n2=10**6)
    while len(calls) < 600:
        a = "".join(rng.choices("abc", k=rng.randint(1, 20)))
        if len(calls) % 3 == 0:
            b = a[: rng.randint(1, len(a))]
            n1 = rng.randint(10, 1000000)
            n2 = rng.randint(1, 10)
        else:
            b = "".join(rng.choices("abcd", k=rng.randint(1, 20)))
            n1 = rng.randint(1, 80)
            n2 = rng.randint(1, 20)
        add(s1=a, n1=n1, s2=b, n2=n2)
    return list(calls)[:600]
