from __future__ import annotations
import random

EXAMPLE_CALLS = [
    "candidate(ranks=[13, 2, 3, 1, 9], suits=['a', 'a', 'a', 'a', 'a'])",
    "candidate(ranks=[4, 4, 2, 4, 4], suits=['d', 'a', 'a', 'b', 'c'])",
    "candidate(ranks=[10, 10, 2, 12, 9], suits=['a', 'b', 'c', 'a', 'd'])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    flushes = {EXAMPLE_CALLS[0]}
    triples = {EXAMPLE_CALLS[1]}
    pairs = {EXAMPLE_CALLS[2]}
    high_cards: set[str] = set()

    while len(flushes) < 150:
        ranks = rng.sample(range(1, 14), 5)
        flushes.add(f"candidate(ranks={ranks!r}, suits={['a'] * 5!r})")
    while len(triples) < 150:
        rank, other1, other2 = rng.sample(range(1, 14), 3)
        ranks = [rank, rank, rank, other1, other2]
        suits = rng.sample(list("abcd"), 3) + [rng.choice("abcd"), rng.choice("abcd")]
        triples.add(f"candidate(ranks={ranks!r}, suits={suits!r})")
    while len(pairs) < 150:
        rank, other1, other2, other3 = rng.sample(range(1, 14), 4)
        ranks = [rank, rank, other1, other2, other3]
        suits = rng.sample(list("abcd"), 2) + [rng.choice("abcd") for _ in range(3)]
        pairs.add(f"candidate(ranks={ranks!r}, suits={suits!r})")
    while len(high_cards) < 150:
        ranks = rng.sample(range(1, 14), 5)
        suits = [rng.choice("abcd") for _ in range(5)]
        if len(set(suits)) == 1:
            suits[-1] = "b" if suits[0] != "b" else "a"
        high_cards.add(f"candidate(ranks={ranks!r}, suits={suits!r})")

    assert len(flushes) == len(triples) == len(pairs) == len(high_cards) == 150
    return sorted(flushes | triples | pairs | high_cards)
