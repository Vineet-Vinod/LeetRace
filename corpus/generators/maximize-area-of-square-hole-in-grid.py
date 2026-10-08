def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases: set[str] = set()

    def add(n: int, m: int, h_bars: list[int], v_bars: list[int]) -> None:
        assert 1 <= n <= 1_000_000_000 and 1 <= m <= 1_000_000_000
        assert 1 <= len(h_bars) <= 100 and 1 <= len(v_bars) <= 100
        assert len(set(h_bars)) == len(h_bars) and len(set(v_bars)) == len(v_bars)
        assert all(2 <= bar <= n + 1 for bar in h_bars)
        assert all(2 <= bar <= m + 1 for bar in v_bars)
        cases.add(f"candidate(n={n}, m={m}, hBars={h_bars!r}, vBars={v_bars!r})")

    add(2, 1, [2, 3], [2])
    add(
        1_000_000_000,
        1_000_000_000,
        [999_999_998, 999_999_999, 1_000_000_000, 1_000_000_001],
        [999_999_998, 999_999_999, 1_000_000_000, 1_000_000_001],
    )

    # Consecutive removed bars create holes from 2x2 through 101x101.
    for index in range(300):
        run_h = 1 + index % 100
        run_v = 1 + (index * 37) % 100
        n = m = 1_000_000_000
        start_h = rng.randint(2, n - run_h + 2)
        start_v = rng.randint(2, m - run_v + 2)
        add(
            n,
            m,
            list(range(start_h, start_h + run_h)),
            list(range(start_v, start_v + run_v)),
        )

    # Spaced bars contain no adjacent removable pair, so these holes stay unit-sized.
    for index in range(300):
        count_h = 1 + index % 100
        count_v = 1 + (index * 13) % 100
        n = m = 1_000_000_000
        h_start = 2 + index % 2
        v_start = 2 + (index + 1) % 2
        add(
            n,
            m,
            [h_start + 2 * offset for offset in range(count_h)],
            [v_start + 2 * offset for offset in range(count_v)],
        )

    while len(cases) < 600:
        n, m = rng.randint(1, 1_000_000_000), rng.randint(1, 1_000_000_000)
        h_bars = rng.sample(range(2, n + 2), min(n, rng.randint(1, 100)))
        v_bars = rng.sample(range(2, m + 2), min(m, rng.randint(1, 100)))
        add(n, m, h_bars, v_bars)

    result = list(cases)
    rng.shuffle(result)
    return result
