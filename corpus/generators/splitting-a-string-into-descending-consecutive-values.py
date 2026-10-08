def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(s='050043')", "candidate(s='9080701')", "candidate(s='1234')"}

    def has_split(text: str) -> bool:
        def search(start: int, previous: int, parts: int) -> bool:
            if start == len(text):
                return parts >= 2
            value = 0
            for end in range(start, len(text)):
                value = value * 10 + int(text[end])
                if value >= previous:
                    break
                if value == previous - 1 and search(end + 1, value, parts + 1):
                    return True
            return False

        return any(search(end, int(text[:end]), 1) for end in range(1, len(text)))

    while len(cases) < 600:
        if rng.random() < 0.55:
            start = rng.randint(10, 9999)
            count = rng.randint(2, 5)
            values = list(range(start, start - count, -1))
            text = "".join(str(value) for value in values)
        else:
            text = "".join(rng.choice("0123456789") for _ in range(rng.randint(1, 20)))
            if has_split(text):
                continue
        assert 1 <= len(text) <= 20 and text.isdigit()
        cases.add(f"candidate(s={text!r})")
    return sorted(cases)
