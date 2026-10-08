import random
import string

EXAMPLES = [
    "candidate(ideas=['coffee', 'donuts', 'time', 'toffee'])",
    "candidate(ideas=['lack', 'back'])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = list(EXAMPLES)
    seen = set(calls)

    def emit(call: str) -> None:
        if call not in seen:
            calls.append(call)
            seen.add(call)

    def add(ideas):
        assert 2 <= len(ideas) <= 50000 and len(set(ideas)) == len(ideas)
        assert all(
            1 <= len(w) <= 10 and set(w) <= set(string.ascii_lowercase) for w in ideas
        )
        emit(f"candidate(ideas={ideas!r})")

    def encode(n):
        text = ""
        for _ in range(4):
            text = chr(97 + n % 26) + text
            n //= 26
        return text

    add([chr(97 + i % 26) + encode(i) for i in range(50000)])
    add(["abcdefghij", "zbcdefghij"])
    add(list(string.ascii_lowercase))
    while len(calls) < 600:
        if rng.random() < 0.25:
            # A shared first letter makes every swap invalid.
            prefix = rng.choice(string.ascii_lowercase)
            ideas = list(
                {
                    prefix + "".join(rng.choices("abcdef", k=rng.randint(1, 6)))
                    for _ in range(rng.randint(2, 35))
                }
            )
        elif rng.random() < 0.4:
            # Disjoint suffix families yield many valid swaps.
            ideas = list(
                {"a" + "".join(rng.choices("abcdef", k=4)) for _ in range(10)}
                | {"b" + "".join(rng.choices("uvwxyz", k=4)) for _ in range(10)}
            )
        else:
            ideas = list(
                {
                    rng.choice("abcde")
                    + "".join(rng.choices("abcd", k=rng.randint(0, 6)))
                    for _ in range(rng.randint(2, 35))
                }
            )
        if len(ideas) < 2:
            continue
        ideas.sort()
        rng.shuffle(ideas)
        add(ideas)
    return calls
