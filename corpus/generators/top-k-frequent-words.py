import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set()
    for i in range(600):
        distinct = 1 + rng.randrange(35)
        words = [
            "".join(
                rng.choice(string.ascii_lowercase) for _ in range(1 + rng.randrange(10))
            )
            for _ in range(distinct)
        ]
        words = list(dict.fromkeys(words))
        pool = words[:]
        pool.extend(rng.choices(words, k=rng.randrange(1, 70)))
        rng.shuffle(pool)
        k = 1 + rng.randrange(len(words))
        cases.add(f"candidate(words={pool!r}, k={k})")
    unique = [
        "".join(chr(97 + (index // divisor) % 26) for divisor in (676, 26, 1))
        for index in range(250)
    ]
    boundary = [word for word in unique for _ in (0, 1)]
    cases.add(f"candidate(words={boundary!r}, k=250)")
    cases.add(f"candidate(words={unique!r}, k=1)")
    return sorted(cases)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(words=['i', 'love', 'leetcode', 'i', 'love', 'coding'], k=2)",
    "candidate(words=['the', 'day', 'is', 'sunny', 'the', 'the', 'the', 'sunny', 'is', 'is'], k=4)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))


_AUDIT_BASE_GENERATE = generate
_AUDIT_BOUNDARY_CALLS = ("candidate(words=['z' * 10, 'a', 'z' * 10, 'a'], k=2)",)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_AUDIT_BASE_GENERATE(seed)) | set(_AUDIT_BOUNDARY_CALLS))
