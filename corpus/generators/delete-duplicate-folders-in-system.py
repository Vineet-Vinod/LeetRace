import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def emit(**values):
        paths = values["paths"]
        tuples = {tuple(p) for p in paths}
        assert 1 <= len(paths) <= 20000 and len(tuples) == len(paths)
        assert sum(len(s) for p in paths for s in p) <= 200000
        assert all(
            1 <= len(p) <= 500
            and all(
                1 <= len(s) <= 10 and s.isascii() and s.isalpha() and s.islower()
                for s in p
            )
            and (len(p) == 1 or tuple(p[:-1]) in tuples)
            for p in paths
        )
        call = (
            "candidate("
            + ", ".join(name + "=" + repr(value) for name, value in values.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    emit(paths=[["a"], ["c"], ["d"], ["a", "b"], ["c", "b"], ["d", "a"]])
    emit(paths=[["a"], ["a", "x"], ["b"], ["b", "x"]])
    emit(paths=[["a"], ["b"]])
    emit(paths=[["a"]])
    emit(paths=[["a"] * i for i in range(1, 501)])

    def name(i):
        return "".join(chr(97 + (i // 26**j) % 26) for j in range(9, -1, -1))

    emit(paths=[[name(i)] for i in range(20000)])
    emit(
        paths=[
            ["a"],
            ["c"],
            ["a", "b"],
            ["c", "b"],
            ["a", "b", "x"],
            ["a", "b", "x", "y"],
            ["w"],
            ["w", "y"],
        ]
    )
    while len(calls) < 600:
        paths = set()
        for _ in range(rng.randint(3, 30)):
            path = tuple(rng.choice("abcde") for _ in range(rng.randint(1, 6)))
            paths.update(path[:i] for i in range(1, len(path) + 1))
        if len(calls) % 2 == 0:
            suffix = [rng.choice("xyz") for _ in range(rng.randint(1, 4))]
            for root in ["p", "q"]:
                path = (root, *suffix)
                paths.update(path[:i] for i in range(1, len(path) + 1))
        ordered = [list(p) for p in sorted(paths)]
        rng.shuffle(ordered)
        emit(paths=ordered)
    return calls
