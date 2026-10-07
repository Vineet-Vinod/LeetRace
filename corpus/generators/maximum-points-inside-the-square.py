import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    alphabet = string.ascii_lowercase
    while len(cases) < 600:
        n = rng.randint(1, 60)
        coords = set()
        points = []
        while len(points) < n:
            point = (rng.randint(-100, 100), rng.randint(-100, 100))
            if point not in coords:
                coords.add(point)
                points.append(list(point))
        tags = "".join(rng.choice(alphabet[:10]) for _ in range(n))
        key = (tuple(map(tuple, points)), tags)
        if key not in seen:
            seen.add(key)
            assert len(coords) == n and len(tags) == n and tags.islower()
            cases.append(f"candidate(points={points!r}, s={tags!r})")
    return cases
