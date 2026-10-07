import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[str, ...]] = {
        ("abc", "xyz"),
        ("abc",),
        ("a", "b", "c"),
        ("z" * 1000,),
        tuple("a" for _ in range(1000)),
    }
    alphabet = string.ascii_lowercase[:8]
    while len(cases) < 600:
        count = rng.randint(1, 15)
        values = tuple(
            "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 15)))
            for _ in range(count)
        )
        cases.add(values)
    assert all(
        1 <= len(values) <= 1000
        and 1 <= sum(map(len, values)) <= 1000
        and all(
            1 <= len(value) <= 1000 and set(value) <= set(string.ascii_lowercase)
            for value in values
        )
        for values in cases
    )
    return [f"candidate(strs={list(values)!r})" for values in sorted(cases)]
