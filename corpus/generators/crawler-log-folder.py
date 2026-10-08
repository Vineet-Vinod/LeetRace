import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    choices = ["../", "./", "a/", "folder2/", "z9/"]
    while len(calls) < 600:
        logs = [rng.choice(choices) for _ in range(rng.randint(1, 1000))]
        calls.add(f"candidate(logs={logs!r})")
    return sorted(calls)
