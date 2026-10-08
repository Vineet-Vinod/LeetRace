def _generate_base(seed: int = 0) -> list[str]:
    import random
    import string

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        folders = set()
        while len(folders) < rng.randint(1, 50):
            depth = rng.randint(1, 5)
            parts = [
                "".join(
                    rng.choice(string.ascii_lowercase[:8])
                    for _ in range(rng.randint(1, 5))
                )
                for _ in range(depth)
            ]
            folders.add("/" + "/".join(parts))
        folder = sorted(folders)
        assert all(path.startswith("/") and len(path) <= 100 for path in folder)
        cases.add(f"candidate(folder={folder!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    examples = [
        "candidate(folder=['/a', '/a/b', '/c/d', '/c/d/e', '/c/f'])",
        "candidate(folder=['/a', '/a/b/c', '/a/b/d'])",
        "candidate(folder=['/a/b/c', '/a/b/ca', '/a/b/d'])",
    ]
    calls = sorted(set(calls + examples))

    def encode(index: int) -> str:
        letters = ""
        while index:
            index, remainder = divmod(index, 26)
            letters = chr(ord("a") + remainder) + letters
        return letters or "a"

    boundary = (
        f"candidate(folder={[f'/folder{encode(index)}' for index in range(40000)]!r})"
    )
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
