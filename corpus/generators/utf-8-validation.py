import random


def generate(seed: int = 0) -> list[str]:
    """Mix random byte sequences with valid UTF-8 encodings of Unicode strings."""
    rng = random.Random(seed)
    calls: list[str] = [f"candidate(data={[0] * 20_000!r})", "candidate(data=[255])"]
    seen: set[str] = set(calls)
    index = 0

    while len(calls) < 300:
        text = "".join(
            chr(rng.choice([rng.randrange(0xD800), rng.randrange(0xE000, 0x110000)]))
            for _ in range(1 + index % 20)
        )
        data = list(text.encode("utf-8"))
        assert 1 <= len(data) <= 2 * 10**4 and all(0 <= byte <= 255 for byte in data)
        call = f"candidate(data={data!r})"
        index += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)

    while len(calls) < 600:
        data = [rng.randrange(256) for _ in range(1 + index % 50)]
        call = f"candidate(data={data!r})"
        index += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
