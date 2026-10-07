import random


def generate(seed: int = 0) -> list[str]:
    r = random.Random(seed)
    cases = []
    seen = set()

    def reverse(n):
        return int(str(n)[::-1])

    positives = set()
    for x in range(50_001):
        v = x + reverse(x)
        if v <= 100_000:
            positives.add(v)
    negatives = set()
    for n in range(0, 1500):
        if n not in positives:
            negatives.add(n)
    for n in sorted(positives)[:300] + sorted(negatives)[:300]:
        if n not in seen:
            seen.add(n)
            cases.append(f"candidate(num={n})")
    while len(cases) < 600:
        n = r.randint(0, 100_000)
        if n not in seen:
            seen.add(n)
            cases.append(f"candidate(num={n})")
    cases.append("candidate(num=100000)")
    return cases
