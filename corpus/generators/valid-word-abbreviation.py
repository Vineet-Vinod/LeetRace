import random
import string

_STATEMENT_EXAMPLES = (
    "candidate(word='internationalization', abbr='i12iz4n')",
    "candidate(word='apple', abbr='a2e')",
)


def generate(seed: int = 0) -> list[str]:
    """Generate lowercase words of length 1..10 and abbreviations of length 1..10."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        word = "".join(
            rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, 10))
        )
        if rng.randrange(2):
            pieces: list[str] = []
            index = 0
            while index < len(word):
                if rng.randrange(2):
                    skipped = rng.randint(1, len(word) - index)
                    pieces.append(str(skipped))
                    index += skipped
                else:
                    pieces.append(word[index])
                    index += 1
            abbr = "".join(pieces)
        else:
            abbr = "".join(
                rng.choice(string.ascii_lowercase + string.digits)
                for _ in range(rng.randint(1, 10))
            )
        call = f"candidate(word={word!r}, abbr={abbr!r})"
        if call not in seen:
            calls.append(call)
            seen.add(call)
    return calls


_BASE_GENERATE = generate


def generate(seed: int = 0) -> list[str]:
    calls = list(_STATEMENT_EXAMPLES)
    seen = set(calls)
    for call in _BASE_GENERATE(seed):
        if call not in seen:
            calls.append(call)
            seen.add(call)
    limit = globals().get("DOMAIN_SIZE", 600)
    if len(calls) < limit:
        raise ValueError("Generator did not produce enough distinct cases")
    return calls[:limit]
