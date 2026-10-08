import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set()
    chars = string.ascii_letters + string.digits + ".:"
    for i in range(600):
        if i % 3 == 0:
            parts = [str(rng.randrange(256)) for _ in range(4)]
            if i % 9 == 0:
                parts[rng.randrange(4)] = "0" + str(rng.randrange(1, 10))
            text = ".".join(parts)
        elif i % 3 == 1:
            parts = [
                "".join(
                    rng.choice("0123456789abcdefABCDEF")
                    for _ in range(1 + rng.randrange(4))
                )
                for _ in range(8)
            ]
            text = ":".join(parts)
        else:
            text = "".join(rng.choice(chars) for _ in range(1 + rng.randrange(35)))
        cases.add(f"candidate(queryIP={text!r})")
    return sorted(cases)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(queryIP='172.16.254.1')",
    "candidate(queryIP='2001:0db8:85a3:0:0:8A2E:0370:7334')",
    "candidate(queryIP='256.256.256.256')",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
