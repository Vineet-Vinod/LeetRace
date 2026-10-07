import random
import string

EXAMPLES = [
    "candidate(words=['alex', 'loves', 'leetcode'])",
    "candidate(words=['catg', 'ctaagt', 'gcta', 'ttca', 'atgcatc'])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = list(EXAMPLES)
    seen = set(calls)

    def emit(call: str) -> None:
        if call not in seen:
            calls.append(call)
            seen.add(call)

    def add(words):
        assert 1 <= len(words) <= 12 and len(set(words)) == len(words)
        assert all(
            1 <= len(w) <= 20 and set(w) <= set(string.ascii_lowercase) for w in words
        )
        assert all(
            a not in b
            for i, a in enumerate(words)
            for j, b in enumerate(words)
            if i != j
        )
        emit(f"candidate(words={words!r})")

    add(["a"])
    add(["a", "b"])
    add([c * 20 for c in string.ascii_lowercase[:12]])
    add(
        [
            "abcdefghijk",
            "bcdefghijkl",
            "cdefghijklm",
            "defghijklmn",
            "efghijklmno",
            "fghijklmnop",
            "ghijklmnopq",
            "hijklmnopqr",
            "ijklmnopqrs",
            "jklmnopqrst",
            "klmnopqrstu",
            "lmnopqrstuv",
        ]
    )
    while len(calls) < 600:
        count = rng.randint(1, 6)
        length = rng.randint(2, 8)
        words = set()
        while len(words) < count:
            words.add("".join(rng.choices("abcde", k=length)))
        words = sorted(words)
        rng.shuffle(words)
        add(words)
    return calls
