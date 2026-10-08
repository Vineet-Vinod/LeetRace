import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        rows, columns = rng.randint(1, 50), rng.randint(1, 50)
        image = [[rng.randint(0, 20) for _ in range(columns)] for _ in range(rows)]
        sr, sc, color = (
            rng.randrange(rows),
            rng.randrange(columns),
            rng.randint(0, 65535),
        )
        assert 0 <= image[sr][sc] < 2**16 and 0 <= color < 2**16
        calls.add(f"candidate(image={image!r}, sr={sr}, sc={sc}, color={color})")
    return sorted(calls)
