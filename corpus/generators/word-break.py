import random


def generate(seed: int = 0) -> list[str]:
    """Mix guaranteed segmentable and unsegmentable strings with unique legal dictionaries."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    index = 0
    while len(calls) < 600:
        if index % 2 == 0:
            length = 1 + (index // 2) % 300
            pieces: list[str] = []
            remaining = length
            while remaining:
                size = rng.randint(1, min(20, remaining))
                pieces.append("".join(rng.choice("abcde") for _ in range(size)))
                remaining -= size
            source = "".join(pieces)
            words = set(pieces)
            while len(words) < min(1 + index % 15, 20):
                words.add(
                    "".join(rng.choice("abcde") for _ in range(1 + rng.randrange(20)))
                )
        else:
            length = 1 + (index // 2) % 300
            source = "z" + "".join(rng.choice("abcde") for _ in range(length - 1))
            words = {
                "".join(rng.choice("abcde") for _ in range(1 + rng.randrange(20)))
                for _ in range(1 + index % 15)
            }
            if not words:
                words = {"a"}
        dictionary = sorted(words)
        assert 1 <= len(source) <= 300
        assert 1 <= len(dictionary) <= 1000 and len(set(dictionary)) == len(dictionary)
        assert all(1 <= len(word) <= 20 and word.islower() for word in dictionary)
        call = f"candidate(s={source!r}, wordDict={dictionary!r})"
        index += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
