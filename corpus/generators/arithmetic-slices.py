import random


_MIN_VALUE = -1000
_MAX_VALUE = 1000
_MAX_LENGTH = 5000


def _arithmetic_progression(rng: random.Random, length: int) -> list[int]:
    if length == 1:
        return [rng.randint(_MIN_VALUE, _MAX_VALUE)]
    max_step = (_MAX_VALUE - _MIN_VALUE) // (length - 1)
    step = rng.randint(-max_step, max_step)
    span = step * (length - 1)
    if span >= 0:
        start = rng.randint(_MIN_VALUE, _MAX_VALUE - span)
    else:
        start = rng.randint(_MIN_VALUE - span, _MAX_VALUE)
    result = [start + index * step for index in range(length)]
    assert all(_MIN_VALUE <= value <= _MAX_VALUE for value in result)
    return result


def generate(seed: int = 0) -> list[str]:
    """All array values and lengths obey the original bounds; long progressions are constructed inside them."""
    rng = random.Random(seed)
    arrays = {
        (1,),
        (1, 2, 3, 4),
        (7, 7, 7, 7),
        tuple([-1000] * _MAX_LENGTH),
        tuple(_MIN_VALUE + index for index in range(2001)),
        tuple(_MAX_VALUE - index for index in range(2001)),
        tuple(
            _MIN_VALUE if index % 2 == 0 else _MAX_VALUE for index in range(_MAX_LENGTH)
        ),
    }
    while len(arrays) < 600:
        length = rng.randint(1, 100)
        if rng.random() < 0.55:
            values = _arithmetic_progression(rng, length)
        else:
            values = [rng.randint(_MIN_VALUE, _MAX_VALUE) for _ in range(length)]
        arrays.add(tuple(values))
    assert len(arrays) == 600
    assert all(1 <= len(values) <= _MAX_LENGTH for values in arrays)
    assert all(
        _MIN_VALUE <= value <= _MAX_VALUE for values in arrays for value in values
    )
    return [f"candidate(nums={list(values)!r})" for values in sorted(arrays)]
