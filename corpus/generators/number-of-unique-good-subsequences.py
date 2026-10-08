import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(binary: str) -> None:
        assert 1 <= len(binary) <= 100000 and set(binary) <= {"0", "1"}
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in [("binary", binary)])
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(binary="001")
    add(binary="0" * 100000)
    add(binary="1" * 100000)
    add(binary="01" * 50000)
    add(binary="001")
    add(binary="11")
    add(binary="101")
    while len(calls) < 600:
        binary = "".join(rng.choices("01", k=rng.randint(1, 100)))
        add(binary=binary)
    return calls
