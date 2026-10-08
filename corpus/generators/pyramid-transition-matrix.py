import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        ("BCD", ("BCC", "CDE", "CEA", "FFF")),
        ("AAAA", ("AAB", "AAC", "BCD", "BBE", "DEF")),
    }
    patterns = [a + b + c for a in "ABCDEF" for b in "ABCDEF" for c in "ABCDEF"]
    while len(cases) < 600:
        bottom = "".join(rng.choice("ABCDEF") for _ in range(rng.randint(2, 6)))
        allowed = tuple(rng.sample(patterns, rng.randint(0, 60)))
        cases.add((bottom, allowed))
    return [
        f"candidate(bottom={bottom!r}, allowed={list(allowed)!r})"
        for bottom, allowed in cases
    ]
