import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**args) -> None:
        s, p = args["s"], args["p"]
        assert 0 <= len(s) <= 2000 and 0 <= len(p) <= 2000
        assert set(s) <= set("abcdefghijklmnopqrstuvwxyz") and set(p) <= set(
            "abcdefghijklmnopqrstuvwxyz?*"
        )
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in args.items())
            + ")"
        )
        calls[call] = None

    add(s="aa", p="a")
    add(s="aa", p="*")
    add(s="cb", p="?a")
    add(s="", p="")
    add(s="", p="*" * 2000)
    add(s="a" * 2000, p="?" * 2000)
    add(s="a" * 1999 + "b", p="*" + "a" * 1998 + "c")
    add(s="aa", p="a")
    add(s="aa", p="*")
    add(s="cb", p="?a")
    while len(calls) < 600:
        s = "".join(rng.choices("abc", k=rng.randint(0, 60)))
        mode = len(calls) % 3
        if mode == 0:
            # Replace individual characters by ? or *
            # The star can absorb that character.
            p = "".join(rng.choice([char, "?", "*"]) for char in s)
        elif mode == 1:
            p = "d" * rng.randint(1, 60)
        else:
            p = "".join(rng.choices("abc?*", k=rng.randint(0, 60)))
        add(s=s, p=p)
    return list(calls)[:600]
