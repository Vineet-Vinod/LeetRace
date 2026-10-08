import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    alphabet = string.ascii_lowercase[:6]
    while len(cases) < 600:
        s = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 80)))
        indices = sorted(rng.sample(range(len(s)), rng.randint(1, min(12, len(s)))))
        sources = []
        targets = []
        for index in indices:
            length = rng.randint(1, min(5, len(s) - index))
            sources.append(
                s[index : index + length]
                if rng.random() < 0.6
                else "".join(rng.choice(alphabet) for _ in range(length))
            )
            targets.append(
                "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 5)))
            )
        key = (s, tuple(indices), tuple(sources), tuple(targets))
        if key not in seen:
            seen.add(key)
            assert len(indices) == len(sources) == len(targets) and len(
                set(indices)
            ) == len(indices)
            cases.append(
                f"candidate(s={s!r}, indices={indices!r}, sources={sources!r}, targets={targets!r})"
            )
    return cases
