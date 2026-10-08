import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[str, str]] = {
        ("cba", "abcd"),
        ("bcafg", "abcd"),
        ("a", "aaaa"),
        ("z", "abc"),
    }
    while len(cases) < 600:
        order = "".join(rng.sample(string.ascii_lowercase, rng.randint(1, 26)))
        s = "".join(
            rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, 200))
        )
        cases.add((order, s))
    assert all(
        1 <= len(order) <= 26
        and len(set(order)) == len(order)
        and set(order) <= set(string.ascii_lowercase)
        and 1 <= len(s) <= 200
        and set(s) <= set(string.ascii_lowercase)
        for order, s in cases
    )
    return [f"candidate(order={order!r}, s={s!r})" for order, s in sorted(cases)]
