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

    def case(a):
        assert 1 <= len(a) <= 100000 and all(1 <= x <= 1000000000 for x in a)
        add(nums=a)

    for a in (
        [1],
        [1, 2, 3, 4],
        [6, 5, 7, 8],
        [8, 7, 6, 6],
        list(range(1, 100001)),
        [1000000000] * 100000,
    ):
        case(a)
    while len(calls) < 600:
        a = [rng.randint(1, 40) for _ in range(rng.randint(1, 60))]
        mode = len(calls) % 4
        if mode == 0:
            a = sorted(set(a))
        if mode == 1:
            a.sort(reverse=True)
        case(a)
    assert len(calls) == 600
    return calls
