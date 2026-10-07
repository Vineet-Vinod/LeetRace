def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    people = list(range(500))
    preferences = [
        [other for other in range(500) if other != person] for person in people
    ]
    for order in preferences:
        rng.shuffle(order)
    rng.shuffle(people)
    pairs = [[people[i], people[i + 1]] for i in range(0, 500, 2)]
    cases = {f"candidate(n=500,preferences={preferences!r},pairs={pairs!r})"}
    while len(cases) < 600:
        n = 2 * rng.randint(1, 20)
        prefs = []
        for person in range(n):
            order = rng.sample([other for other in range(n) if other != person], n - 1)
            prefs.append(order)
        shuffled = list(range(n))
        rng.shuffle(shuffled)
        pairings = [[shuffled[i], shuffled[i + 1]] for i in range(0, n, 2)]
        assert 2 <= n <= 500 and n % 2 == 0
        assert all(len(prefs[i]) == n - 1 and i not in prefs[i] for i in range(n))
        assert len({person for pair in pairings for person in pair}) == n
        cases.add(f"candidate(n={n},preferences={prefs!r},pairs={pairings!r})")
    return sorted(cases)
