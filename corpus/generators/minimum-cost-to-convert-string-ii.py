import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def emit(**values):
        source, target = values["source"], values["target"]
        original, changed, cost = values["original"], values["changed"], values["cost"]
        assert 1 <= len(source) == len(target) <= 1000 and all(
            s.isascii() and s.isalpha() and s.islower()
            for s in [source, target] + original + changed
        )
        assert 1 <= len(original) == len(changed) == len(cost) <= 100
        assert all(
            1 <= len(a) == len(b) <= len(source) and a != b and 1 <= c <= 1000000
            for a, b, c in zip(original, changed, cost)
        )
        call = (
            "candidate("
            + ", ".join(name + "=" + repr(value) for name, value in values.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    emit(source="a", target="b", original=["a"], changed=["b"], cost=[1])
    emit(source="a", target="b", original=["a"], changed=["b"], cost=[1000000])
    emit(source="a", target="a", original=["a"], changed=["b"], cost=[1000000])
    emit(
        source="a" * 1000,
        target="b" * 1000,
        original=["a" * 1000] * 100,
        changed=["b" * 1000] * 100,
        cost=list(range(1, 101)),
    )
    emit(
        source="abcdefgh",
        target="addddddd",
        original=["bcd", "defgh"],
        changed=["ddd", "ddddd"],
        cost=[100, 1578],
    )
    while len(calls) < 600:
        n = rng.randint(2, 25)
        mode = len(calls) % 3
        source = "".join(rng.choices("abc", k=n))
        target = source if mode == 0 else "".join(rng.choices("abc", k=n))
        original = []
        changed = []
        cost = []
        for _ in range(rng.randint(1, 15)):
            length = rng.randint(1, min(5, n))
            a = "".join(rng.choices("abc", k=length))
            b = "".join(rng.choices("abc", k=length))
            if a == b:
                b = ("a" if b[0] != "a" else "b") + b[1:]
            original.append(a)
            changed.append(b)
            cost.append(rng.randint(1, 100))
        if mode == 1:
            original.extend(["a", "b", "c"])
            changed.extend(["b", "c", "a"])
            cost.extend([2, 3, 4])
        emit(
            source=source, target=target, original=original, changed=changed, cost=cost
        )
    return calls
