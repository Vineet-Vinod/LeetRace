import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {"abbxxxxzzy", "abc", "abcdddeeeeaabbbcd"}
    cases.add("a" * 1000)
    cases.add("a")
    while len(cases) < 600:
        cases.add(
            "".join(
                rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, 1000))
            )
        )
    return [f"candidate(s={value!r})" for value in cases]
