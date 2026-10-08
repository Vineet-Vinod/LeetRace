import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        ("parker", "morris", "parser"),
        ("hello", "world", "hold"),
        ("leetcode", "programs", "sourcecode"),
    }
    while len(cases) < 600:
        n = rng.randint(1, 1000)
        s1 = "".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(n))
        s2 = "".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(n))
        base = "".join(
            rng.choice("abcdefghijklmnopqrstuvwxyz")
            for _ in range(rng.randint(1, 1000))
        )
        cases.add((s1, s2, base))
    return [f"candidate(s1={a!r}, s2={b!r}, baseStr={base!r})" for a, b, base in cases]
