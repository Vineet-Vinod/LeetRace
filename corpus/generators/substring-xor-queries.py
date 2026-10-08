import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set()
    for i in range(600):
        length = 1 + rng.randrange(120)
        s = "".join(rng.choice("01") for _ in range(length))
        queries = []
        for _ in range(1 + rng.randrange(20)):
            if rng.randrange(2):
                start = rng.randrange(length)
                end = min(length, start + 1 + rng.randrange(31))
                value = int(s[start:end], 2)
            else:
                value = rng.randrange(1 << 31)
            first = rng.randrange(1 << 30)
            queries.append([first, first ^ value])
        cases.add(f"candidate(s={s!r}, queries={queries!r})")
    return sorted(cases)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(s='0101', queries=[[12, 8]])",
    "candidate(s='101101', queries=[[0, 5], [1, 2]])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
