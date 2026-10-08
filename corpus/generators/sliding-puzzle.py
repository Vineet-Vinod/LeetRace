import itertools


def generate(seed: int = 0) -> list[str]:
    # Every board is a permutation of the six labels: 6! = 720 legal inputs.
    return [
        f"candidate(board={[list(p[:3]), list(p[3:])]!r})"
        for p in itertools.permutations(range(6))
    ]
