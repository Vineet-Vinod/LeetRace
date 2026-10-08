import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = {"candidate(s='aabcbc')", "candidate(s='abccba')"}
    while len(calls) < 600:
        if rng.random() < 0.5:
            pieces = ["abc" for _ in range(rng.randint(1, 100))]
            s = "".join(pieces)
            # Applying valid insertions at random boundaries preserves validity.
            for _ in range(rng.randint(0, 20)):
                position = rng.randrange(len(s) + 1)
                s = s[:position] + "abc" + s[position:]
        else:
            s = "".join(rng.choice("abc") for _ in range(3 * rng.randint(1, 50)))
        calls.add(f"candidate(s={s!r})")
    return sorted(calls)
