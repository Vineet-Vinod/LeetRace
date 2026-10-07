import random
import string

EXAMPLES = [
    "candidate(wordsContainer=['abcd', 'bcd', 'xbcd'], wordsQuery=['cd', 'bcd', 'xyz'])",
    "candidate(wordsContainer=['abcdefgh', 'poiuygh', 'ghghgh'], wordsQuery=['gh', 'acbfgh', 'acbfegh'])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = list(EXAMPLES)
    seen = set(calls)

    def emit(call: str) -> None:
        if call not in seen:
            calls.append(call)
            seen.add(call)

    def add(container, queries):
        for words in (container, queries):
            assert 1 <= len(words) <= 10000 and sum(map(len, words)) <= 500000
            assert all(
                1 <= len(w) <= 5000 and set(w) <= set(string.ascii_lowercase)
                for w in words
            )
        emit(f"candidate(wordsContainer={container!r}, wordsQuery={queries!r})")

    add(["a" * 50] * 10000, ["b" * 50] * 10000)
    add(["a" * 5000, "b" * 4999 + "a"], ["a" * 5000, "c" * 4999 + "a"])
    while len(calls) < 600:
        container = [
            "".join(rng.choices("abcd", k=rng.randint(1, 15)))
            for _ in range(rng.randint(1, 20))
        ]
        queries = []
        for _ in range(rng.randint(1, 15)):
            if rng.random() < 0.7:
                w = rng.choice(container)
                queries.append(
                    "".join(rng.choices("xyz", k=rng.randint(0, 5)))
                    + w[-rng.randint(1, len(w)) :]
                )
            else:
                queries.append("".join(rng.choices("abcxyz", k=rng.randint(1, 15))))
        add(container, queries)
    return calls
