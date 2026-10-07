import random


def valid_string(rng: random.Random) -> str:
    group_count = rng.randint(1, 30)
    pair_index = rng.randrange(group_count)
    groups: list[str] = []
    previous = ""
    for index in range(group_count):
        digit = rng.choice([value for value in "0123456789" if value != previous])
        width = 2 if index == pair_index else 3
        groups.append(digit * width)
        previous = digit
    return "".join(groups)


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        "000111000",
        "00011111222",
        "011100022233",
        "00",
        "000",
        "00" + "".join(str(index % 10) * 3 for index in range(1, 333)),
    }
    while len(cases) < 600:
        cases.add(
            "".join(rng.choice("0123456789") for _ in range(rng.randint(1, 1000)))
        )
        cases.add(valid_string(rng))
    return [f"candidate(s={value!r})" for value in cases]
