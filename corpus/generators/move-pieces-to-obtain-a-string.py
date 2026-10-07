import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: list[str] = []
    seen: set[tuple[str, str]] = set()

    def add(start: str, target: str) -> None:
        if (start, target) not in seen:
            assert 1 <= len(start) == len(target) <= 100_000
            assert set(start) <= {"L", "R", "_"} and set(target) <= {"L", "R", "_"}
            seen.add((start, target))
            cases.append(f"candidate(start={start!r}, target={target!r})")

    add("_L__R__R_", "L______RR")
    add("R_L_", "__LR")
    add("_R", "R_")

    for index in range(300):
        left_count = index + 1
        right_count = rng.randint(1, 500)
        start = "_" + "L" * left_count + "R" * right_count + "_"
        target = "L" * left_count + "_" + "R" * right_count + "_"
        add(start, target)

    for _ in range(300):
        length = rng.randint(3, 100)
        start = "L" + "".join(rng.choice("LR_") for _ in range(length - 1))
        # A changed first non-blank piece guarantees impossibility.
        target = "R" + "".join(rng.choice("LR_") for _ in range(length - 1))
        add(start, target)

    add(
        "_" + "L" * 49_999 + "R" * 49_999 + "_", "L" * 49_999 + "_" + "R" * 49_999 + "_"
    )
    return cases
