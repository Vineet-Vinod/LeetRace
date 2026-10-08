def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    orders = {
        "".join("abcdefghijklmnopqrstuvwxyz"),
        "".join(reversed("abcdefghijklmnopqrstuvwxyz")),
    }
    while len(orders) < 100:
        order = list("abcdefghijklmnopqrstuvwxyz")
        rng.shuffle(order)
        orders.add("".join(order))
    cases = set()
    cases.add(
        (
            tuple(f"word{chr(97 + i // 26)}{chr(97 + i % 26)}" for i in range(100)),
            "abcdefghijklmnopqrstuvwxyz",
        )
    )
    for order in sorted(orders):
        rank = {c: i for i, c in enumerate(order)}
        words = sorted(
            {
                "".join(rng.choice(order[:6]) for _ in range(rng.randint(1, 8)))
                for _ in range(8)
            },
            key=lambda w: [rank[c] for c in w],
        )
        cases.add((tuple(words), order))
    while len(cases) < 600:
        order = list("abcdefghijklmnopqrstuvwxyz")
        rng.shuffle(order)
        order = "".join(order)
        words = tuple(
            "".join(rng.choice("abcxyz") for _ in range(rng.randint(1, 10)))
            for _ in range(rng.randint(1, 20))
        )
        cases.add((words, order))
    return [f"candidate(words={list(w)!r}, order={o!r})" for w, o in sorted(cases)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(words=['hello', 'leetcode'], order='hlabcdefgijkmnopqrstuvwxyz')",
    "candidate(words=['word', 'world', 'row'], order='worldabcefghijkmnpqstuvxyz')",
    "candidate(words=['apple', 'app'], order='abcdefghijklmnopqrstuvwxyz')",
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
