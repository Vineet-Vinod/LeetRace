def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    sequences = [
        int("".join(str(digit) for digit in range(start, start + length)))
        for length in range(2, 10)
        for start in range(1, 11 - length)
    ]
    possible = {
        "candidate(low=100,high=300)",
        "candidate(low=123456789,high=123456789)",
    }
    impossible = {"candidate(low=10,high=10)"}
    while len(possible) < 300:
        value = rng.choice(sequences)
        low = max(10, value - rng.randint(0, 1000))
        high = min(10**9, value + rng.randint(0, 1000))
        assert 10 <= low <= high <= 10**9
        possible.add(f"candidate(low={low},high={high})")
    while len(impossible) < 300:
        prefix = str(rng.randint(1, 9)) * 2
        suffix = "".join(str(rng.randint(0, 9)) for _ in range(rng.randint(1, 7)))
        value = int(prefix + suffix)
        impossible.add(f"candidate(low={value},high={value})")
    return sorted(possible | impossible)
