import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def emit(**values):
        words = values["words"]
        assert 1 <= len(words) <= 100 and all(
            1 <= len(w) <= 100 and w.isascii() and w.islower() and w.isalpha()
            for w in words
        )
        call = (
            "candidate("
            + ", ".join(name + "=" + repr(value) for name, value in values.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    emit(words=["wrt", "wrf", "er", "ett", "rftt"])
    emit(words=["z", "x", "z"])
    emit(words=["abc", "ab"])
    emit(words=["a" * 100] * 100)
    emit(words=["abcdefghijklmnopqrstuvwxyz" * 3 + "abcdefghijklmnopqrstuv"])
    while len(calls) < 600:
        alphabet = list("abcdef")
        rng.shuffle(alphabet)
        rank = {c: i for i, c in enumerate(alphabet)}
        words = [
            "".join(rng.choices(alphabet, k=rng.randint(1, 10)))
            for _ in range(rng.randint(1, 25))
        ]
        if len(calls) % 3:
            words.sort(key=lambda w: [rank[c] for c in w])
        emit(words=words)
    return calls
