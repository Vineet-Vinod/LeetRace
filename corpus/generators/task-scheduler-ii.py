import random


def generate(seed: int = 0) -> list[str]:
    """Generate nonempty positive task IDs and 1 <= space <= len(tasks)."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        tasks = [rng.randrange(1, 30) for _ in range(1 + i % 60)]
        space = 1 + (i * 7) % len(tasks)
        call = f"candidate(tasks={tasks!r}, space={space})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
