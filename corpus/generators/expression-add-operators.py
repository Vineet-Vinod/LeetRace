import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**data) -> None:
        s, target = data["num"], data["target"]
        assert (
            1 <= len(s) <= 10
            and s.isascii()
            and s.isdigit()
            and -2147483648 <= target <= 2147483647
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
        {"num": "123", "target": 6},
        {"num": "232", "target": 8},
        {"num": "3456237490", "target": 9191},
    ]:
        add(**example)
    add(num="0000000000", target=1)
    add(num="9999999999", target=2147483647)
    add(num="1234567890", target=-2147483648)
    add(num="105", target=5)
    add(num="00", target=0)
    while len(calls) < 600:
        length = rng.randint(1, 6)
        num = "".join(rng.choice("000123456789") for _ in range(length))
        mode = len(calls) % 4
        target = rng.randint(-500, 500)
        if mode == 0:
            target = sum(map(int, num))
        if mode == 1:
            target = 1
            for c in num:
                target *= int(c)
        if mode == 2:
            target = int(num)
        add(num=num, target=target)
    assert len(calls) == 600
    return calls
