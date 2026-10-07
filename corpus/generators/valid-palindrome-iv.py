def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(s='abcdba')",
        f"candidate(s={'a' * 100000!r})",
        f"candidate(s={'bbb' + 'a' * 99997!r})",
    }
    while len(cases) < 600:
        if rng.random() < 0.5:
            length = rng.randint(1, 100)
            half = [rng.choice("abcdef") for _ in range(length // 2)]
            chars = half + ([rng.choice("abcdef")] if length % 2 else []) + half[::-1]
            for _ in range(rng.randint(0, 2)):
                if length >= 2:
                    index = rng.randrange(length // 2)
                    chars[index] = "z" if chars[index] != "z" else "y"
            text = "".join(chars)
        else:
            length = rng.randint(6, 100)
            chars = [rng.choice("abcdef") for _ in range(length)]
            for index in range(min(3, length // 2 + length % 2)):
                chars[index] = "z"
                chars[length - 1 - index] = "a"
            text = "".join(chars)
        assert 1 <= len(text) <= 100000 and text.islower()
        cases.add(f"candidate(s={text!r})")
    return sorted(cases)
