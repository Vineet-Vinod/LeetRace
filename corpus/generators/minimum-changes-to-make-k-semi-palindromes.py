import random
import string

EXAMPLES = [
    "candidate(s='abcac', k=2)",
    "candidate(s='abcdef', k=2)",
    "candidate(s='aabbaa', k=3)",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = list(EXAMPLES)
    seen = set(calls)

    def emit(call: str) -> None:
        if call not in seen:
            calls.append(call)
            seen.add(call)

    def add(s, k):
        assert (
            2 <= len(s) <= 200
            and 1 <= k <= len(s) // 2
            and set(s) <= set(string.ascii_lowercase)
        )
        emit(f"candidate(s={s!r}, k={k})")

    add("a" * 200, 1)
    add("abcdefghijklmnopqrstuvwxyz" * 7 + "abcdefghijklmnopqr", 100)
    add("ab" * 100, 50)
    while len(calls) < 600:
        n = rng.randint(2, 28)
        k = rng.randint(1, n // 2)
        if rng.random() < 0.35:
            # Concatenated length-two palindromes provide a zero-change family.
            s = "".join(rng.choice("abcd") * 2 for _ in range(k))
            if len(s) < 2:
                continue
        else:
            s = "".join(rng.choices("abcdef", k=n))
        add(s, k)
    return calls
