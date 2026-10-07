import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        a, b = kwargs["str1"], kwargs["str2"]
        assert 1 <= len(a) == len(b) <= 10000
        assert set(a + b) <= set("abcdefghijklmnopqrstuvwxyz")
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(str1="aabcc", str2="ccdee")
    add(str1="leetcode", str2="codeleet")
    add(str1="a" * 10000, str2="z" * 10000)
    add(str1="abcdefghijklmnopqrstuvwxyz", str2="bcdefghijklmnopqrstuvwxyza")
    add(str1="abcdefghijklmnopqrstuvwxyz", str2="abcdefghijklmnopqrstuvwxyz")
    while len(calls) < 600:
        n = rng.randint(1, 100)
        a = "".join(rng.choices("abcdef", k=n))
        if len(calls) % 2:
            mapping = {
                c: rng.choice("abcdefghijklmnopqrstuvwxyz") for c in sorted(set(a))
            }
            b = "".join(mapping[c] for c in a)
        else:
            b = "".join(rng.choices("abcdef", k=n))
        add(str1=a, str2=b)
    return calls
