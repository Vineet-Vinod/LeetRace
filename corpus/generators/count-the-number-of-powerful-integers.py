import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(start: int, finish: int, limit: int, s: str) -> None:
        assert 1 <= start <= finish <= 10**15 and 1 <= limit <= 9
        assert (
            1 <= len(s) <= len(str(finish))
            and s[0] != "0"
            and all("0" <= d <= str(limit) for d in s)
        )
        call = (
            "candidate("
            + ", ".join(
                f"{key}={value!r}"
                for key, value in [
                    ("start", start),
                    ("finish", finish),
                    ("limit", limit),
                    ("s", s),
                ]
            )
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(start=1, finish=6000, limit=4, s="124")
    add(start=1, finish=10**15, limit=9, s="1")
    add(start=10**15, finish=10**15, limit=1, s="1000000000000000")
    add(start=1000, finish=2000, limit=4, s="3000")
    add(start=1, finish=6000, limit=4, s="124")
    add(start=15, finish=215, limit=6, s="10")
    add(start=1000, finish=2000, limit=4, s="3000")
    while len(calls) < 600:
        limit = rng.randint(1, 9)
        finish = rng.choice([rng.randint(1, 10000), rng.randint(10**10, 10**15)])
        length = rng.randint(1, len(str(finish)))
        s = str(rng.randint(1, limit)) + "".join(
            str(rng.randint(0, limit)) for _ in range(length - 1)
        )
        start = rng.choice([1, rng.randint(1, finish)])
        add(start=start, finish=finish, limit=limit, s=s)
    return calls
