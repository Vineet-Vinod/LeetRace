def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        f"candidate(messages={['word'] * 10000!r}, senders={['Sender'] * 10000!r})",
        "candidate(messages=['a b', 'c d'], senders=['Alice', 'alice'])",
        "candidate(messages=['one two three', 'four five six'], senders=['A', 'Z'])",
        "candidate(messages=['x'], senders=['a'])",
    }
    alphabet = "AbcXYZ"
    while len(cases) < 600:
        n = rng.randint(1, 30)
        names = [rng.choice(["Alice", "alice", "Bob", "Zed", "a"]) for _ in range(n)]
        messages = [
            " ".join(rng.choice(alphabet) for _ in range(rng.randint(1, 10)))
            for _ in range(n)
        ]
        assert len(messages) == len(names) and all(
            1 <= len(x) <= 100 and x == x.strip() for x in messages
        )
        assert all(1 <= len(x) <= 10 and x.isalpha() for x in names)
        cases.add(f"candidate(messages={messages!r}, senders={names!r})")
    return sorted(cases)
