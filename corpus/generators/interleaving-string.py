import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    alphabet = string.ascii_lowercase[:4]
    while len(cases) < 600:
        s1 = "".join(rng.choice(alphabet) for _ in range(rng.randint(0, 30)))
        s2 = "".join(rng.choice(alphabet) for _ in range(rng.randint(0, 30)))
        if rng.random() < 0.5:
            i = j = 0
            out = []
            while i < len(s1) or j < len(s2):
                if i < len(s1) and (j == len(s2) or rng.random() < 0.5):
                    out.append(s1[i])
                    i += 1
                else:
                    out.append(s2[j])
                    j += 1
            s3 = "".join(out)
        else:
            s3 = "".join(rng.choice(alphabet) for _ in range(len(s1) + len(s2)))
        key = (s1, s2, s3)
        if key not in seen:
            seen.add(key)
            assert len(s1) + len(s2) == len(s3) and all(
                c in alphabet for c in s1 + s2 + s3
            )
            cases.append(f"candidate(s1={s1!r}, s2={s2!r}, s3={s3!r})")
    return cases
