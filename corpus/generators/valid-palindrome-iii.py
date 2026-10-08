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

    def case(s, k):
        assert (
            1 <= len(s) <= 1000 and all("a" <= c <= "z" for c in s) and 1 <= k <= len(s)
        )
        add(s=s, k=k)

    case("abcdeca", 2)
    case("abbababa", 1)
    case("a" * 1000, 1)
    case("abcdefghijklmnopqrstuvwxyz" * 38 + "abcdefghijkl", 1)
    case("abcdefghijklmnopqrstuvwxyz" * 38 + "abcdefghijkl", 1000)
    while len(calls) < 600:
        mode = len(calls) % 3
        a = "".join(rng.choice("abcdef") for _ in range(rng.randint(2, 50)))
        if mode == 0:
            s = a + a[::-1]
            k = 1
        elif mode == 1:
            s = a + "z" + a[::-1]
            k = rng.randint(1, len(s))
        else:
            s = a
            k = rng.randint(1, max(1, len(s) // 4))
        case(s, k)
    assert len(calls) == 600
    return calls
