import random


def generate(seed: int = 0) -> list[str]:
    """Generate lowercase strings with zero or one odd character count, and strings with two odd counts."""
    rng = random.Random(seed)
    true_cases = set()
    false_cases = set()
    alphabet = "abcdef"

    while len(true_cases) < 300:
        pairs = [rng.choice(alphabet) for _ in range(rng.randint(0, 40))]
        chars = [char for pair in pairs for char in (pair, pair)]
        if rng.random() < 0.5 or not chars:
            chars.append(rng.choice(alphabet))
        rng.shuffle(chars)
        true_cases.add("".join(chars) or "a")
    while len(false_cases) < 300:
        chars = [rng.choice(alphabet) for _ in range(rng.randint(0, 40))]
        first, second = rng.sample(alphabet, 2)
        chars.extend([first, second])
        chars.extend(
            char
            for pair in [rng.choice(alphabet) for _ in range(rng.randint(0, 30))]
            for char in (pair, pair)
        )
        rng.shuffle(chars)
        false_cases.add("".join(chars))

    cases = true_cases | false_cases | {"code", "aab", "carerac"}
    calls = [f"candidate(s={value!r})" for value in cases]
    calls.append(f"candidate(s={'a' * 4999 + 'b'!r})")
    return calls
