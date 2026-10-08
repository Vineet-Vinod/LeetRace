import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**data) -> None:
        s, k = data["s"], data["k"]
        assert (
            2 <= len(s) <= 2000
            and 2 <= k <= 2000
            and len(s) < k * 8
            and all("a" <= c <= "z" for c in s)
        )
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in data.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for example in [
        {"s": "letsleetcode", "k": 2},
        {"s": "bb", "k": 2},
        {"s": "ab", "k": 2},
    ]:
        add(**example)
    add(s="z" * 2000, k=2000)
    add(s=("abcdefg" * 285) + "abcde", k=251)
    add(s="abcdefghijklmn", k=2)
    while len(calls) < 600:
        k = rng.randint(2, 25)
        if len(calls) % 3:
            word = "".join(rng.choice("abcxyz") for _ in range(rng.randint(1, 6)))
            chunks = []
            for _ in range(k):
                for c in word:
                    if rng.random() < 0.15:
                        chunks.append(rng.choice("def"))
                    chunks.append(c)
            s = "".join(chunks)
            if len(s) >= 8 * k:
                s = word * k
        else:
            s = "".join(
                rng.choice("abcdefghijklmnopqrstuvwxyz")
                for _ in range(rng.randint(2, min(100, 8 * k - 1)))
            )
        add(s=s, k=k)
    assert len(calls) == 600
    return calls
