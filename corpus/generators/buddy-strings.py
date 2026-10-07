import random


def generate(seed: int = 0) -> list[str]:
    """Use lowercase strings of length 1..20000 with both swappable and impossible pairs."""
    rng = random.Random(seed)
    true_cases = set()
    false_cases = set()

    while len(true_cases) < 300:
        if rng.random() < 0.15:
            chars = [rng.choice("abc") for _ in range(rng.randint(2, 40))]
            chars[1] = chars[0]
            value = "".join(chars)
            true_cases.add((value, value))
            continue
        chars = [rng.choice("abc") for _ in range(rng.randint(2, 40))]
        first, second = rng.sample(range(len(chars)), 2)
        if chars[first] == chars[second]:
            chars[second] = "a" if chars[first] != "a" else "b"
        source = "".join(chars)
        chars[first], chars[second] = chars[second], chars[first]
        true_cases.add((source, "".join(chars)))

    while len(false_cases) < 300:
        source = "".join(rng.choice("abc") for _ in range(rng.randint(1, 40)))
        target = "".join(rng.choice("abc") for _ in range(rng.randint(1, 40)))
        if len(source) != len(target):
            false_cases.add((source, target))
            continue
        differences = [i for i, (a, b) in enumerate(zip(source, target)) if a != b]
        can_swap = (
            len(differences) == 2
            and source[differences[0]] == target[differences[1]]
            and source[differences[1]] == target[differences[0]]
        )
        can_swap = can_swap or (not differences and len(set(source)) < len(source))
        if not can_swap:
            false_cases.add((source, target))

    cases = true_cases | false_cases | {("ab", "ba"), ("ab", "ab"), ("aa", "aa")}
    calls = [f"candidate(s={source!r}, goal={target!r})" for source, target in cases]
    calls.append(f"candidate(s={'a' * 20000!r}, goal={'a' * 19998 + 'bb'!r})")
    return calls
