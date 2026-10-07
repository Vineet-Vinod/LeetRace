import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set()

    def add(citations: list[int]) -> None:
        assert 1 <= len(citations) <= 100_000
        assert all(0 <= value <= 1000 for value in citations)
        assert citations == sorted(citations)
        cases.add(f"candidate(citations={citations!r})")

    add([0])
    add([1000])
    add([0, 0, 0])
    add([1, 2, 100])
    add([1000] * 100_000)
    add([0] * 100_000)
    add([value for value in range(1001) for _ in range(99)])
    while len(cases) < 600:
        size = rng.randint(1, 1000)
        citations = sorted(rng.randint(0, 1000) for _ in range(size))
        add(citations)
    return sorted(cases)
