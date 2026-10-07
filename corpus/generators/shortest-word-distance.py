def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        (("practice", "makes", "perfect", "coding", "makes"), "coding", "practice"),
        (("a", "b", "a", "c"), "a", "b"),
    }
    while len(cases) < 600:
        words = tuple(
            rng.choice(("a", "b", "c", "d")) for _ in range(rng.randint(2, 100))
        )
        word1, word2 = rng.sample(("a", "b", "c", "d"), 2)
        words = list(words)
        i, j = rng.sample(range(len(words)), 2)
        words[i] = word1
        words[j] = word2
        cases.add((tuple(words), word1, word2))
    for distance in range(1, 101):
        words = ("left",) + ("filler",) * (distance - 1) + ("right",)
        cases.add((words, "left", "right"))
    max_words = ["a"] * 29998 + ["b", "c"]
    cases.add((tuple(max_words), "b", "c"))
    return [
        f"candidate(wordsDict={list(w)!r}, word1={a!r}, word2={b!r})"
        for w, a, b in sorted(cases)
    ]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(wordsDict=['practice', 'makes', 'perfect', 'coding', 'makes'], word1='coding', word2='practice')",
    "candidate(wordsDict=['practice', 'makes', 'perfect', 'coding', 'makes'], word1='makes', word2='coding')",
]
_ORIGINAL_GENERATE = generate


def generate(seed: int = 0) -> list[str]:
    import ast

    calls = _ORIGINAL_GENERATE(seed) + _STATEMENT_EXAMPLE_CALLS
    unique = {}
    for call in calls:
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        unique.setdefault(key, call)
    return [unique[key] for key in sorted(unique)]
