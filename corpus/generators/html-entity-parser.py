import random


def generate(seed: int = 0) -> list[str]:
    """Generate arbitrary strings over text and supported/unsupported entity spellings."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    pieces = [
        "plain",
        "&quot;",
        "&apos;",
        "&amp;",
        "&gt;",
        "&lt;",
        "&frasl;",
        "&unknown;",
        "&amp",
        ";",
    ]
    while len(calls) < 600:
        text = "".join(rng.choice(pieces) for _ in range(1 + i % 20))
        call = f"candidate(text={text!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
