import random


def generate(seed: int = 0) -> list[str]:
    """Lowercase strings and nonempty lowercase dictionary words satisfy the task input rules."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        s = "".join(rng.choice("abcde") for _ in range(1 + i % 40))
        dictionary = sorted(
            {
                "".join(rng.choice("abcde") for _ in range(1 + rng.randrange(8)))
                for _ in range(1 + i % 12)
            }
        )
        if not dictionary:
            dictionary = ["a"]
        call = f"candidate(s={s!r}, dictionary={dictionary!r})"
        i += 1
        assert 1 <= len(s) <= 50
        assert 1 <= len(dictionary) <= 50
        assert len(dictionary) == len(set(dictionary))
        assert all(1 <= len(word) <= 50 and word.islower() for word in dictionary)
        assert s.islower()
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return sorted(calls)
