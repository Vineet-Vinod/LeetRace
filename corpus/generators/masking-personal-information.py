import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    separators = ["-", " ", "(", ")", "+"]
    while len(calls) < 600:
        if rng.random() < 0.5:
            local = "".join(
                rng.choice(string.ascii_letters) for _ in range(rng.randint(2, 14))
            )
            domain = (
                "".join(
                    rng.choice(string.ascii_letters) for _ in range(rng.randint(2, 10))
                )
                + "."
                + "".join(
                    rng.choice(string.ascii_letters) for _ in range(rng.randint(2, 8))
                )
            )
            value = local + "@" + domain
        else:
            country_length = rng.randint(0, 3)
            digits = "".join(
                rng.choice("0123456789") for _ in range(10 + country_length)
            )
            list(digits)
            max_separators = 20 - len(digits) - (1 if country_length else 0)
            gaps = rng.sample(
                range(1, len(digits)),
                rng.randint(0, min(max_separators, len(digits) - 1)),
            )
            value = ("+" if country_length else "") + "".join(
                (rng.choice(separators[:-1]) if index in gaps else "") + digit
                for index, digit in enumerate(digits)
            )
        calls.add(f"candidate(s={value!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(s='1(234)567-890')",
    "candidate(s='LeetCode@LeetCode.com')",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
