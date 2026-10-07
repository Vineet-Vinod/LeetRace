def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(palindrome='a')", "candidate(palindrome='abba')"}
    while len(cases) < 600:
        n = rng.randint(1, 100)
        half = "".join(
            rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range((n + 1) // 2)
        )
        s = half + (half[:-1] if n % 2 else half)[::-1]
        cases.add(f"candidate(palindrome={s!r})")
    return sorted(cases)
