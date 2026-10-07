import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**args) -> None:
        s, p = args["s"], args["p"]
        assert 1 <= len(s) <= 20 and 1 <= len(p) <= 20
        assert set(s) <= set("abcdefghijklmnopqrstuvwxyz") and set(p) <= set(
            "abcdefghijklmnopqrstuvwxyz.*"
        )
        assert all(i > 0 and p[i - 1] != "*" for i, char in enumerate(p) if char == "*")
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in args.items())
            + ")"
        )
        calls[call] = None

    add(s="aa", p="a")
    add(s="aa", p="a*")
    add(s="ab", p=".*")
    add(s="a" * 20, p="a*" * 10)
    add(s="a" * 19 + "b", p="a*" * 9 + "b*")
    add(s="aa", p="a")
    add(s="aa", p="a*")
    add(s="ab", p=".*")
    while len(calls) < 600:
        if len(calls) % 2 == 0:
            # Each token is expanded to form a matching nonempty string.
            tokens = []
            chars = []
            for _ in range(rng.randint(1, 8)):
                char = rng.choice("abc")
                atom = rng.choice([char, "."])
                repeat = rng.choice([True, False])
                tokens.append(atom + ("*" if repeat else ""))
                chars.append(char * rng.randint(1, 2) if repeat else char)
            s, p = "".join(chars), "".join(tokens)
        else:
            s = "".join(rng.choices("abc", k=rng.randint(1, 20)))
            p = "".join(
                rng.choice("abcd.") + rng.choice(["", "*"])
                for _ in range(rng.randint(1, 10))
            )
        add(s=s, p=p)
    return list(calls)[:600]
