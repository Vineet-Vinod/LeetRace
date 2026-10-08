import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(s: str) -> None:
        assert 0 <= len(s) <= 50000 and all("a" <= c <= "z" for c in s)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in [("s", s)])
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(s="")
    add(s="aacecaaa")
    add(s="abcd")
    add(s="a" * 50000)
    add(s="ab" * 25000)
    add(s="a" * 49999 + "b")
    add(s="aacecaaa")
    add(s="abcd")
    while len(calls) < 600:
        s = "".join(rng.choices("abcde", k=rng.randint(0, 100)))
        if len(calls) % 3 == 0:
            s = s + s[::-1]
        add(s=s)
    return calls
