import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    alphabet = string.ascii_lowercase
    while len(cases) < 600:
        n = rng.randint(1, 60)
        creators = [
            "".join(rng.choice(alphabet[:8]) for _ in range(rng.randint(1, 5)))
            for _ in range(n)
        ]
        ids = []
        for i in range(n):
            value = i
            name = ""
            while True:
                name = alphabet[value % 26] + name
                value //= 26
                if value == 0:
                    break
            ids.append(name)
        views = [rng.randint(0, 100000) for _ in range(n)]
        key = (tuple(creators), tuple(ids), tuple(views))
        if key not in seen:
            seen.add(key)
            assert (
                len(creators) == len(ids) == len(views)
                and len(set(ids)) == n
                and all(0 <= v <= 100000 for v in views)
            )
            cases.append(
                f"candidate(creators={creators!r}, ids={ids!r}, views={views!r})"
            )
    return cases
