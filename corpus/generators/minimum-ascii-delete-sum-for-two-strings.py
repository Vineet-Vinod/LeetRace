import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {("sea", "eat"), ("delete", "leet")}
    while len(cases) < 600:
        cases.add(
            (
                "".join(
                    rng.choice("abcdefghijklmnopqrstuvwxyz")
                    for _ in range(rng.randint(1, 100))
                ),
                "".join(
                    rng.choice("abcdefghijklmnopqrstuvwxyz")
                    for _ in range(rng.randint(1, 100))
                ),
            )
        )
    return [f"candidate(s1={a!r}, s2={b!r})" for a, b in cases]
