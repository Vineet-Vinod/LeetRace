import random


_MAX_ENCODED_LENGTH = 100
_MAX_INDEX = 10**9
_MAX_DECODED_LENGTH = 2**63 - 1


def _decoded_length(encoded: str) -> int:
    length = 0
    for char in encoded:
        if char.isdigit():
            length *= int(char)
        else:
            length += 1
    return length


def generate(seed: int = 0) -> list[str]:
    """Encoded strings have length 2..100, start with a letter, and keep decoded length below 2^63."""
    rng = random.Random(seed)
    samples = {
        ("leet2code3", 10),
        ("ha22", 5),
        ("a2345678999999999999999", 1),
        ("a2", 2),
        ("a" + "9" * 19, _MAX_INDEX),
    }
    while len(samples) < 600:
        pieces = [rng.choice("abcdefghijklmnopqrstuvwxyz")]
        encoded_length = 1
        decoded_length = 1
        target_length = rng.randint(2, 100)
        while encoded_length < target_length:
            if rng.random() < 0.45 and decoded_length <= _MAX_DECODED_LENGTH // 9:
                digit = str(rng.randint(2, 9))
                pieces.append(digit)
                decoded_length *= int(digit)
            elif decoded_length < _MAX_DECODED_LENGTH:
                pieces.append(rng.choice("abcdefghijklmnopqrstuvwxyz"))
                decoded_length += 1
            else:
                break
            encoded_length += 1
        encoded = "".join(pieces)
        index = rng.randint(1, min(_MAX_INDEX, decoded_length))
        samples.add((encoded, index))

    calls = [f"candidate(s={encoded!r}, k={index})" for encoded, index in samples]
    assert len(calls) == len(set(calls)) == 600
    for encoded, index in samples:
        length = _decoded_length(encoded)
        assert 2 <= len(encoded) <= _MAX_ENCODED_LENGTH
        assert encoded[0].islower()
        assert all(char.islower() or char in "23456789" for char in encoded)
        assert 1 <= index <= min(_MAX_INDEX, length)
        assert length <= _MAX_DECODED_LENGTH
    return sorted(calls)
