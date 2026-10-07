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

    def case(arr, k):
        # Construct lower/higher from positive arr and positive k. This proves existence.
        assert 1 <= len(arr) <= 1000 and k > 0 and all(x > 0 for x in arr)
        a = [x - k for x in arr] + [x + k for x in arr]
        assert all(1 <= x <= 1000000000 for x in a)
        rng.shuffle(a)
        add(nums=a)

    case([3, 7, 11], 1)
    case([2, 2], 1)
    case([220], 215)
    case([500000000] * 1000, 499999999)
    case(list(range(2, 1002)), 1)
    while len(calls) < 600:
        k = rng.randint(1, 1000)
        case([rng.randint(k + 1, k + 300) for _ in range(rng.randint(1, 45))], k)
    assert len(calls) == 600
    return calls
