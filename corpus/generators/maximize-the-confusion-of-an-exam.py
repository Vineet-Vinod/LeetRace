import random


def generate(seed: int = 0) -> list[str]:
    """Generate nonempty T/F answer keys and k in [1,n]."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        answer = "".join(rng.choice("TF") for _ in range(1 + i % 60))
        k = 1 + (i * 7) % len(answer)
        call = f"candidate(answerKey={answer!r}, k={k})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
