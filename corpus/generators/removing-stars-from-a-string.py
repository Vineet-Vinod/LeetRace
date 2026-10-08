import random


def generate(seed: int = 0) -> list[str]:
    """Construct strings by only appending a star when an unremoved letter exists to its left."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        output = []
        stack_depth = 0
        for _ in range(1 + i % 60):
            if stack_depth and rng.random() < 0.3:
                output.append("*")
                stack_depth -= 1
            else:
                output.append(rng.choice("abcdefghijklmnopqrstuvwxyz"))
                stack_depth += 1
        s = "".join(output)
        assert all(ch == "*" or ch.islower() for ch in s)
        call = f"candidate(s={s!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
