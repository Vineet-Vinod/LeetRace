import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(ring: str, key: str) -> None:
        assert 1 <= len(ring) <= 100 and 1 <= len(key) <= 100
        assert all("a" <= c <= "z" for c in ring + key) and set(key) <= set(ring)
        call = (
            "candidate("
            + ", ".join(
                f"{key}={value!r}" for key, value in [("ring", ring), ("key", key)]
            )
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(ring="godding", key="gd")
    add(ring="a" * 100, key="a" * 100)
    add(ring="ab" * 50, key="ba" * 50)
    add(ring="abcdefghijklmnopqrstuvwxyz" * 3 + "abcdefghijklmnopqrstuv", key="zy" * 50)
    add(ring="godding", key="gd")
    add(ring="godding", key="godding")
    while len(calls) < 600:
        ring = "".join(rng.choices("abcdef", k=rng.randint(1, 35)))
        key = "".join(rng.choices(ring, k=rng.randint(1, 40)))
        add(ring=ring, key=key)
    return calls
