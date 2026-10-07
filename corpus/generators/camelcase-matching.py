import random


def generate(seed: int = 0) -> list[str]:
    """Generate valid English-letter queries/patterns of length at most 100."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    i = 0
    while len(calls) < 600:
        pattern = "".join(rng.choice("ABCDEF") for _ in range(1 + i % 5))
        queries: list[str] = []
        for j in range(1 + i % 12):
            chars: list[str] = []
            for char in pattern:
                chars.append(char)
                chars.extend(rng.choice("abcdef") for _ in range(rng.randrange(3)))
            if j % 3 == 0:
                chars.insert(rng.randrange(len(chars) + 1), rng.choice("XYZ"))
            queries.append("".join(chars))
        assert 1 <= len(pattern) <= 100 and all(1 <= len(q) <= 100 for q in queries)
        call = f"candidate(queries={queries!r}, pattern={pattern!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
