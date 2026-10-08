import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    names = ["a", "b2", "...", "....", "_tmp"]
    while len(calls) < 600:
        parts = [rng.choice(names + [".", ".."]) for _ in range(rng.randint(1, 30))]
        path = "/" + "/".join(parts) + ("/" if rng.random() < 0.5 else "")
        calls.add(f"candidate(path={path!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(path='/.../a/../b/c/../d/./')",
    "candidate(path='/home/')",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
