import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        def render(value):
            # Repeat only immutable scalar values; nested input lists retain distinct identities.
            if isinstance(value, list):
                if (
                    len(value) >= 1000
                    and isinstance(value[0], (int, str))
                    and all(x == value[0] for x in value)
                ):
                    return f"[{value[0]!r}] * {len(value)}"
                return "[" + ", ".join(render(x) for x in value) + "]"
            return repr(value)

        call = (
            "candidate("
            + ", ".join(f"{key}={render(value)}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    def case(a, k):
        assert 1 <= len(a) <= 100 and all(1 <= x <= 10000 for x in a) and 1 <= k <= 100
        add(nums=a, k=k)

    case([1, 2, 3], 3)
    case([2, 3, 3], 5)
    case([1, 2, 3], 7)
    case([10000] * 100, 100)
    case([1] * 100, 100)
    while len(calls) < 600:
        a = [rng.randint(1, 20) for _ in range(rng.randint(1, 30))]
        k = rng.randint(1, 100)
        if len(calls) % 2:
            # Guaranteed positive inner subsequence sum.
            k = sum(rng.sample(a, min(len(a), rng.randint(1, 4))))
        case(a, k)
    assert len(calls) == 600
    return calls
