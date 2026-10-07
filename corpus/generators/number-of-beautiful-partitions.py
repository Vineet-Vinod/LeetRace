import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**args) -> None:
        s, k, min_length = args["s"], args["k"], args["minLength"]
        assert (
            1 <= k <= len(s) <= 1000
            and 1 <= min_length <= len(s)
            and set(s) <= set("123456789")
        )
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in args.items())
            + ")"
        )
        calls[call] = None

    add(s="23542185131", k=3, minLength=2)
    add(s="23542185131", k=3, minLength=3)
    add(s="3312958", k=3, minLength=1)
    add(s="21" * 500, k=500, minLength=2)
    add(s="2" + "1" * 999, k=1, minLength=1000)
    add(s="1" * 1000, k=1000, minLength=1000)
    add(s="23542185131", k=3, minLength=2)
    add(s="3312958", k=3, minLength=1)
    while len(calls) < 600:
        if len(calls) % 2 == 0:
            k = rng.randint(1, 10)
            min_length = rng.randint(1, 6)
            s = "".join(
                rng.choice("2357")
                + "".join(
                    rng.choices(
                        "123456789", k=max(0, min_length - 2) + rng.randint(0, 4)
                    )
                )
                + rng.choice("14689")
                for _ in range(k)
            )
        else:
            s = "".join(rng.choices("123456789", k=rng.randint(1, 50)))
            k = rng.randint(1, len(s))
            min_length = rng.randint(1, len(s))
        add(s=s, k=k, minLength=min_length)
    return list(calls)[:600]
