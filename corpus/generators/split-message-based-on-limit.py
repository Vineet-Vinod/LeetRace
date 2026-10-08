import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**data) -> None:
        s, limit = data["message"], data["limit"]
        assert (
            1 <= len(s) <= 10000
            and set(s) <= set("abcdefghijklmnopqrstuvwxyz ")
            and 1 <= limit <= 10000
        )
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in data.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for example in [
        {"message": "this is really a very awesome message", "limit": 9},
        {"message": "short message", "limit": 15},
    ]:
        add(**example)
    add(message="a" * 10000, limit=10000)
    add(message=" " * 10000, limit=1)
    add(message="abcde" * 2000, limit=15)
    for length in [1, 8, 9, 10, 18, 19, 20, 98, 99, 100, 998, 999, 1000]:
        for limit in [5, 6, 7, 8, 9, 10, 12]:
            add(message="a" * length, limit=limit)
    while len(calls) < 600:
        message = "".join(rng.choice("abc xyz") for _ in range(rng.randint(1, 200)))
        add(
            message=message,
            limit=rng.choice([1, 5, 6, 7, 8, 9, 10, 15, 10000, rng.randint(1, 100)]),
        )
    assert len(calls) == 600
    return calls
