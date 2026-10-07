def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(pattern='abab',s='redblueredblue')"}
    while len(cases) < 600:
        pattern = "".join(rng.choice("abcd") for _ in range(rng.randint(1, 10)))
        s = "".join(rng.choice("abcde") for _ in range(rng.randint(1, 20)))
        cases.add(f"candidate(pattern={pattern!r},s={s!r})")
    return sorted(cases)
