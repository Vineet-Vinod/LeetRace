import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: list[str] = []
    seen: set[str] = set()

    def add(value: str) -> None:
        if value not in seen:
            assert 1 <= len(value) <= 100_000
            assert set(value) <= {"H", "."}
            seen.add(value)
            cases.append(f"candidate(hamsters={value!r})")

    add("H." * 50_000)
    add(".H" * 50_000)
    add("H" * 100_000)
    add("." * 99_999 + "H")
    for length in range(1, 60):
        for pattern in ("H.", ".H", "H..", ".HH.", "HH."):
            add((pattern * length)[:100])
        add("." * (length - 1) + "H")
        add("H" * length)
        add("H" + "." * (length - 1) + "H")
    while len(cases) < 600:
        add("".join(rng.choice("H.") for _ in range(rng.randint(1, 100))))
    return cases
