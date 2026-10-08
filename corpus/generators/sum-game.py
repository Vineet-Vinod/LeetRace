import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        "5023",
        "25??",
        "?3295???",
        "??",
        "1?",
        "?0?0",
        "9?0?",
        "??11",
        "123456",
        "?" * 100_000,
        "0" * 100_000,
    }
    while len(cases) < 600:
        half = rng.randint(1, 50)
        if rng.random() < 0.5:
            left = "".join(rng.choice("0123456789") for _ in range(half))
            cases.add(left + left)
            continue
        if rng.random() < 0.5:
            half = rng.randrange(2, 51, 2)
            remaining = 9 * half // 2
            digits = []
            for _ in range(half):
                digit = min(9, remaining)
                digits.append(str(digit))
                remaining -= digit
            left = "".join(digits)
            cases.add(left + "?" * half)
            continue
        left_questions = rng.randint(0, half)
        right_questions = rng.randint(0, half)
        while (left_questions - right_questions) % 2 == 0:
            left_questions = rng.randint(0, half)
            right_questions = rng.randint(0, half)
        left = "?" * left_questions + "".join(
            rng.choice("0123456789") for _ in range(half - left_questions)
        )
        right = "?" * right_questions + "".join(
            rng.choice("0123456789") for _ in range(half - right_questions)
        )
        cases.add(left + right)
    assert all(
        2 <= len(num) <= 100_000
        and len(num) % 2 == 0
        and set(num) <= set("0123456789?")
        for num in cases
    )
    return [f"candidate(num={num!r})" for num in sorted(cases)]
