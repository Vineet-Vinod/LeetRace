import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        ("My name is Haley", "My Haley"),
        ("of", "A lot of words"),
        ("Eating right now", "Eating"),
    }
    while len(cases) < 600:
        first = [
            "".join(
                rng.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
                for _ in range(rng.randint(1, 7))
            )
            for _ in range(rng.randint(1, 10))
        ]
        if rng.random() < 0.5:
            start = rng.randint(0, len(first) - 1)
            end = rng.randint(start + 1, len(first))
            second = first[:start] + first[end:]
            if not second:
                second = first[:1]
        else:
            second = [
                "".join(
                    rng.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
                    for _ in range(rng.randint(1, 7))
                )
                for _ in range(rng.randint(1, 10))
            ]
        cases.add((" ".join(first), " ".join(second)))
    calls = []
    for sentence1, sentence2 in sorted(cases):
        assert 1 <= len(sentence1) <= 100 and 1 <= len(sentence2) <= 100
        assert all(
            sentence.strip() and "  " not in sentence
            for sentence in (sentence1, sentence2)
        )
        calls.append(f"candidate(sentence1={sentence1!r}, sentence2={sentence2!r})")
    return calls
