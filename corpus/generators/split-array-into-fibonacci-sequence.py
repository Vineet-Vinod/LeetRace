import random


def generate(seed: int = 0) -> list[str]:
    """Mix random digit strings with strings constructively formed from Fibonacci sequences."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    index = 0

    while len(calls) < 300:
        first = rng.randrange(0, 10_001)
        second = rng.randrange(0, 10_001)
        sequence = [first, second]
        while len(sequence) < 3 or len("".join(map(str, sequence))) < 40:
            next_value = sequence[-1] + sequence[-2]
            if next_value >= 2**31:
                break
            sequence.append(next_value)
            if len("".join(map(str, sequence))) > 40:
                sequence.pop()
                break
        if len(sequence) >= 3:
            number = "".join(map(str, sequence))
            if len(number) <= 40:
                call = f"candidate(num={number!r})"
                if call not in seen:
                    seen.add(call)
                    calls.append(call)
        index += 1

    maximum_length = "9" * 200
    calls.append(f"candidate(num={maximum_length!r})")
    seen.add(calls[-1])

    while len(calls) < 600:
        length = 1 + index % 40
        number = "".join(rng.choice("0123456789") for _ in range(length))
        call = f"candidate(num={number!r})"
        index += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
