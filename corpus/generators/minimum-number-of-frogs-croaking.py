import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        "croakcroak",
        "crcoakroak",
        "croakcrook",
        "croak",
        "ccrrooaakk",
        "croak" * 20_000,
        "c" * 20_000 + "r" * 20_000 + "o" * 20_000 + "a" * 20_000 + "k" * 20_000,
    }
    while len(cases) < 600:
        if rng.random() < 0.55:
            frogs = rng.randint(1, 20)
            text = "".join(stage * frogs for stage in "croak")
        elif rng.random() < 0.5:
            text = "croak" * rng.randint(1, 100)
        else:
            text = "".join(rng.choice("croak") for _ in range(rng.randint(1, 100)))
        cases.add(text)
    assert all(
        1 <= len(text) <= 100_000 and set(text) <= set("croak") for text in cases
    )
    return [f"candidate(croakOfFrogs={text!r})" for text in sorted(cases)]
