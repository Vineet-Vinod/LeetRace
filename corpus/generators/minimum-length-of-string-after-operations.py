import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {"abaacbcbb", "aa"}
    while len(cases) < 600:
        cases.add(
            "".join(
                rng.choice("abcdefghijklmnopqrstuvwxyz")
                for _ in range(rng.randint(1, 100))
            )
        )
    return [f"candidate(s={s!r})" for s in cases]
