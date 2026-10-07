import random

EXAMPLES = ["candidate(low='50', high='100')", "candidate(low='0', high='0')"]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = list(EXAMPLES)
    seen = set(calls)

    def emit(call: str) -> None:
        if call not in seen:
            calls.append(call)
            seen.add(call)

    def add(low, high):
        assert (
            1 <= len(low) <= 15
            and 1 <= len(high) <= 15
            and low.isdigit()
            and high.isdigit()
        )
        assert str(int(low)) == low and str(int(high)) == high and int(low) <= int(high)
        emit(f"candidate(low={low!r}, high={high!r})")

    add("0", "999999999999999")
    add("100000000000000", "999999999999999")
    add("999999999999999", "999999999999999")
    while len(calls) < 600:
        a = rng.choice([rng.randint(0, 10000), rng.randint(0, 999999999999999)])
        b = rng.choice([a, a + rng.randint(1, 10000), rng.randint(a, 999999999999999)])
        b = min(b, 999999999999999)
        add(str(a), str(b))
    return calls
