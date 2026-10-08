import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        calls[
            "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        ] = None

    # Every call has exactly four cards in [1, 9]; enumerate 495 multisets,
    # then include ordered hands because card ordering is legal input.
    from itertools import combinations_with_replacement

    for cards in combinations_with_replacement(range(1, 10), 4):
        add(cards=list(cards))
    while len(calls) < 600:
        cards = [rng.randint(1, 9) for _ in range(4)]
        assert len(cards) == 4 and all(1 <= x <= 9 for x in cards)
        add(cards=cards)
    assert len(calls) == 600
    return list(calls)
