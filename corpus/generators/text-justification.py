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

    def case(words, width):
        assert 1 <= len(words) <= 300 and 1 <= width <= 100
        assert all(
            1 <= len(w) <= min(20, width)
            and all(c.isascii() and not c.isspace() for c in w)
            for w in words
        )
        add(words=words, maxWidth=width)

    case(["This", "is", "an", "example", "of", "text", "justification."], 16)
    case(["What", "must", "be", "acknowledgment", "shall", "be"], 16)
    case(["a"] * 300, 1)
    case(["Z" * 20] * 300, 100)
    case(
        [
            "Science",
            "is",
            "what",
            "we",
            "understand",
            "well",
            "enough",
            "to",
            "explain",
            "to",
            "a",
            "computer.",
            "Art",
            "is",
            "everything",
            "else",
            "we",
            "do",
        ],
        20,
    )
    while len(calls) < 600:
        width = rng.randint(1, 100)
        words = [
            "".join(
                rng.choice("abcXYZ.,!?") for _ in range(rng.randint(1, min(20, width)))
            )
            for _ in range(rng.randint(1, 40))
        ]
        case(words, width)
    assert len(calls) == 600
    return calls
