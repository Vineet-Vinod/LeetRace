"""Both lists contain unique lowercase words and share at least one word."""


def _generate_base(seed: int = 0) -> list[str]:
    import random

    r = random.Random(seed)
    alphabet = [chr(97 + i // 26) + chr(97 + i % 26) for i in range(676)]
    cases = set()
    for _ in range(1000):
        pool = r.sample(alphabet, r.randint(5, 60))
        shared = pool[: r.randint(1, len(pool))]
        a = shared + r.sample([x for x in alphabet if x not in pool], r.randint(0, 20))
        b = shared + r.sample(
            [x for x in alphabet if x not in pool and x not in a], r.randint(0, 20)
        )
        r.shuffle(a)
        r.shuffle(b)
        cases.add(f"candidate(list1={a!r}, list2={b!r})")
        if len(cases) >= 600:
            break
    return sorted(cases)


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(
        [
            "candidate(list1=[chr(97 + i // 26) + chr(97 + i % 26) for i in range(1000)], list2=[chr(97 + i // 26) + chr(97 + i % 26) for i in range(1000)])"
        ]
    )
    for call in _generate_base(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(
        [
            "candidate(list1=['Shogun', 'Tapioca Express', 'Burger King', 'KFC'], list2=['Piatti', 'The Grill at Torrey Pines', 'Hungry Hunter Steakhouse', 'Shogun'])",
            "candidate(list1=['Shogun', 'Tapioca Express', 'Burger King', 'KFC'], list2=['KFC', 'Shogun', 'Burger King'])",
            "candidate(list1=['happy', 'sad', 'good'], list2=['sad', 'happy', 'good'])",
        ]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
