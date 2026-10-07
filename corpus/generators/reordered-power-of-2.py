import random


def generate(seed: int = 0) -> list[str]:
    r = random.Random(seed)
    powers = [1 << i for i in range(30)]
    signatures = {"".join(sorted(str(value))) for value in powers}
    positives = set(powers)
    while len(positives) < 300:
        digits = str(r.choice(powers))
        value = int("".join(r.sample(digits, len(digits))))
        positives.add(value)
    negatives = set()
    while len(negatives) < 300:
        value = r.randint(1, 10**9)
        if "".join(sorted(str(value))) not in signatures:
            negatives.add(value)
    values = sorted(positives)[:300] + sorted(negatives)[:300] + [10**9]
    return [f"candidate(n={value})" for value in values]
