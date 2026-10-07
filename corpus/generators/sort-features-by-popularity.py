import random
import string


def name_for(value: int) -> str:
    letters = ""
    while value:
        value, remainder = divmod(value, 26)
        letters = string.ascii_lowercase[remainder] + letters
    return letters or "a"


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[str, ...], tuple[str, ...]]] = {
        (
            ("cooler", "lock", "touch"),
            ("i like cooler cooler", "lock touch cool", "lock cooler"),
        ),
        (("a", "aa", "b", "c"), ("a", "a aa", "a a a a a", "b a")),
        (tuple(name_for(i) for i in range(10_000)), ("x" * 1000,)),
    }
    while len(cases) < 600:
        features = tuple(
            rng.sample([name_for(i) for i in range(100)], rng.randint(1, 15))
        )
        responses = tuple(
            " ".join(rng.sample(list(features), rng.randint(1, len(features))))
            for _ in range(rng.randint(1, 30))
        )
        cases.add((features, responses))
    assert all(
        1 <= len(features) <= 10_000
        and len(set(features)) == len(features)
        and all(
            1 <= len(feature) <= 10 and set(feature) <= set(string.ascii_lowercase)
            for feature in features
        )
        and 1 <= len(responses) <= 100
        and all(
            1 <= len(response) <= 1000
            and "  " not in response
            and not response.startswith(" ")
            and not response.endswith(" ")
            and set(response.replace(" ", "")) <= set(string.ascii_lowercase)
            for response in responses
        )
        for features, responses in cases
    )
    return [
        f"candidate(features={list(features)!r}, responses={list(responses)!r})"
        for features, responses in sorted(cases)
    ]
