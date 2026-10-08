"""Each operation is selected from the currently legal choices, so the score history stays valid."""


def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(1000):
        ops = []
        scores = []
        for j in range(rng.randint(1, 30)):
            choices = (
                ["num"]
                + (["D", "C"] if scores else [])
                + (["+"] if len(scores) >= 2 else [])
            )
            kind = rng.choice(choices)
            if kind == "num":
                value = rng.randint(-1000, 1000)
                ops.append(str(value))
                scores.append(value)
            elif kind == "D":
                ops.append("D")
                scores.append(2 * scores[-1])
            elif kind == "+":
                ops.append("+")
                scores.append(scores[-1] + scores[-2])
            else:
                ops.append("C")
                scores.pop()
        cases.add(f"candidate(operations={ops!r})")
        if len(cases) >= 600:
            break
    return sorted(cases)


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(["candidate(operations=['1'] * 1000)"])
    for call in _generate_base(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(
        [
            "candidate(operations=['5', '2', 'C', 'D', '+'])",
            "candidate(operations=['5', '-2', '4', 'C', 'D', '9', '+', '+'])",
            "candidate(operations=['1', 'C'])",
        ]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
