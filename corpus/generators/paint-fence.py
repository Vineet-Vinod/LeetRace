def generate(seed: int = 0) -> list[str]:
    cases = {(1, colors) for colors in range(1, 501)}
    cases.update((2, colors) for colors in range(1, 101))
    assert len(cases) == 600
    return [f"candidate(n={posts}, k={colors})" for posts, colors in sorted(cases)]
