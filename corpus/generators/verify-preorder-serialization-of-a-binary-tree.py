import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = {
        "#",
        "1,#,#",
        "1,#",
        "#,#",
        "9,3,4,#,#,1,#,#,2,#,6,#,#",
        ",".join(["0"] * 5000),
    }
    while len(cases) < 600:
        rng.randint(1, 25)
        tokens: list[str] = []
        pending = 1
        while pending and len(tokens) < 49:
            pending -= 1
            if rng.random() < 0.35:
                tokens.append("#")
            else:
                tokens.append(str(rng.randint(0, 100)))
                pending += 2
        tokens.extend("#" for _ in range(pending))
        valid = ",".join(tokens)
        cases.add(valid)
        if len(tokens) > 1:
            cases.add(",".join(tokens[:-1]))
        cases.add(valid + ",#")
    cases = {value for value in cases if len(value) <= 10_000}
    assert all(
        1 <= len(value) <= 10_000
        and all(
            token == "#" or token.isdigit() and 0 <= int(token) <= 100
            for token in value.split(",")
        )
        for value in cases
    )
    return [f"candidate(preorder={value!r})" for value in sorted(cases)]
