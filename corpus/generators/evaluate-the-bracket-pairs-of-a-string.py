def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            'candidate(s="(name)is(age)yearsold", knowledge=[["name", "bob"], ["age", "two"]])',
            'candidate(s="x" * 100000, knowledge=[])',
            'candidate(s="x", knowledge=[[chr(97 + i // 17576) + chr(97 + (i // 676) % 26) + chr(97 + (i // 26) % 26) + chr(97 + i % 26), "v"] for i in range(100000)])',
            'candidate(s="(aaaaaaaaaa)", knowledge=[["aaaaaaaaaa", "zzzzzzzzzz"]])',
        ]
    )
    for index in range(600):
        count = index % 20
        keys = ["k" + chr(97 + j % 26) + chr(97 + j // 26) for j in range(count)]
        knowledge = [
            [
                key,
                "".join(
                    rng.choice("abcdefghijklmnopqrstuvwxyz")
                    for _ in range(rng.randint(1, 10))
                ),
            ]
            for key in keys
        ]
        pieces = []
        for _ in range(rng.randint(1, 20)):
            if keys and rng.random() < 0.7:
                pieces.append(f"({rng.choice(keys)})")
            elif rng.random() < 0.5:
                pieces.append(f"({rng.choice('abcxyz')})")
            else:
                pieces.append(
                    "".join(
                        rng.choice("abcdefghijklmnopqrstuvwxyz")
                        for _ in range(rng.randint(1, 10))
                    )
                )
        s = "".join(pieces) or "a"
        cases.add(f"candidate(s={s!r}, knowledge={knowledge!r})")
    while len(cases) < 600:
        s = "".join(
            rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(rng.randint(1, 100))
        )
        cases.add(f"candidate(s={s!r}, knowledge=[])")
    return sorted(cases)
