def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(hand=[1,2,3],groupSize=3)",
        "candidate(hand=[1000000000],groupSize=1)",
        "candidate(hand=[1,2,3,4,5],groupSize=4)",
        f"candidate(hand={list(range(10000))!r},groupSize=1)",
        f"candidate(hand={list(range(0, 20000, 2))!r},groupSize=2)",
    }

    def validate(hand: list[int], groupSize: int) -> None:
        assert 1 <= len(hand) <= 10_000
        assert all(0 <= card <= 1_000_000_000 for card in hand)
        assert 1 <= groupSize <= len(hand)

    while len(cases) < 600:
        if rng.random() < 0.5:
            group_size = rng.randint(1, 8)
            group_count = rng.randint(1, 12)
            hand = []
            for _ in range(group_count):
                start = rng.randint(0, 100_000 - group_size)
                hand.extend(range(start, start + group_size))
            rng.shuffle(hand)
        else:
            group_size = rng.randint(2, 8)
            hand_size = group_size * rng.randint(1, 12)
            hand = [rng.randint(0, 100) for _ in range(hand_size)]
            while len(hand) % group_size:
                hand.pop()
            if rng.random() < 0.5 and hand:
                hand[0] = 1_000_000_000
        validate(hand, group_size)
        cases.add(f"candidate(hand={hand!r},groupSize={group_size})")

    for call in cases:
        eval(call, {"candidate": validate})
    return sorted(cases)
