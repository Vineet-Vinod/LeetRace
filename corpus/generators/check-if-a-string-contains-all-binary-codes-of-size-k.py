import random


def de_bruijn(k: int) -> str:
    work = [0] * (2 * k)
    sequence: list[int] = []

    def visit(position: int, period: int) -> None:
        if position > k:
            if k % period == 0:
                sequence.extend(work[1 : period + 1])
            return
        work[position] = work[position - period]
        visit(position + 1, period)
        for bit in range(work[position - period] + 1, 2):
            work[position] = bit
            visit(position + 1, position)

    visit(1, 1)
    cycle = "".join(map(str, sequence))
    return cycle + cycle[: k - 1]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[str, int]] = {
        ("00110110", 2),
        ("0110", 1),
        ("0110", 2),
        (de_bruijn(18), 18),
        ("0" * 500_000, 20),
    }
    for k in range(1, 10):
        cases.add((de_bruijn(k), k))
        cases.add(("0" * (2**k + k - 2), k))
    while len(cases) < 600:
        k = rng.randint(1, 20)
        if rng.random() < 0.55 and k <= 18:
            s = de_bruijn(k)
        else:
            length = rng.randint(1, 500)
            s = "".join(rng.choice("01") for _ in range(length))
        cases.add((s, k))
    assert all(
        1 <= len(s) <= 500_000 and set(s) <= set("01") and 1 <= k <= 20
        for s, k in cases
    )
    return [f"candidate(s={s!r}, k={k})" for s, k in sorted(cases)]
