import random


def generate(seed: int = 0) -> list[str]:
    r = random.Random(seed)
    vals = {"1", "9", "10", "32", "27346209830709182346"}
    for _ in range(300):
        n = r.randint(1, 100)
        vals.add("".join(str(r.randint(1, 4)) for _ in range(n)))
    for _ in range(300):
        n = r.randint(1, 100)
        vals.add("".join(str(r.randint(1, 9)) for _ in range(n)))
    vals.add("1" * 100_000)
    vals.add("3" * 100_000)
    vals.add("9" * 100_000)
    while len(vals) < 600:
        vals.add("".join(str(r.randint(1, 6)) for _ in range(r.randint(1, 100))))
    return [f"candidate(n={v!r})" for v in sorted(vals)[:600]]
