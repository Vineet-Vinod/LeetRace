"""Seeded unique calls are constructed within the stated input constraints."""


def _generate_base(seed: int = 0) -> list[str]:
    import random

    r = random.Random(seed)
    cases = set()
    for _ in range(1000):
        words = [
            "".join(r.choice("abcd") for _ in range(r.randint(1, 6)))
            for _ in range(r.randint(1, 10))
        ]
        gaps = [r.randint(1, 2) for _ in range(len(words) - 1)]
        text = (" " * r.randint(0, 3)) + (" " * 0)
        text = (
            " " * r.randint(0, 3)
            + "".join(
                w + (" " * gaps[i] if i < len(gaps) else "")
                for i, w in enumerate(words)
            )
            + " " * r.randint(0, 3)
        )
        cases.add(f"candidate(text={text!r})")
        if len(cases) >= 600:
            break
    return sorted(cases)


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(["candidate(text=('a' * 98) + '  ')"])
    for call in _generate_base(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(
        [
            "candidate(text='  this   is  a sentence ')",
            "candidate(text=' practice   makes   perfect')",
        ]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
