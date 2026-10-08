def generate(seed: int = 0) -> list[str]:
    values = set(range(1, 600)) | {100000}
    assert len(values) == 600 and all(1 <= n <= 100000 for n in values)
    return [f"candidate(n={n})" for n in sorted(values)]
