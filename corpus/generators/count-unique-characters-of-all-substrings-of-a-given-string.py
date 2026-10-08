import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**data) -> None:
        s = data["s"]
        assert 1 <= len(s) <= 100000 and all("A" <= c <= "Z" for c in s)
        # Independently compute the promised 32-bit bound from occurrence gaps.
        positions = {c: [-1] for c in set(s)}
        for i, c in enumerate(s):
            positions[c].append(i)
        total = 0
        for indices in positions.values():
            indices.append(len(s))
            total += sum(
                (indices[i] - indices[i - 1]) * (indices[i + 1] - indices[i])
                for i in range(1, len(indices) - 1)
            )
        assert total <= 2147483647
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in data.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for example in [{"s": "ABC"}, {"s": "ABA"}, {"s": "LEETCODE"}]:
        add(**example)
    add(s="A" * 100000)
    add(s=("ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 3847)[:100000])
    add(s="A" * 99999 + "Z")
    while len(calls) < 600:
        alphabet = rng.choice(["A", "AB", "ABC", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"])
        s = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 100)))
        add(s=s)
    assert len(calls) == 600
    return calls
