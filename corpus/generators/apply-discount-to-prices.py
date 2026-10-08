import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    calls.add(
        "candidate(sentence='there are $1 $2 and 5$ candies in the shop', discount=50)"
    )
    calls.add("candidate(sentence='1 2 $3 4 $5 $6 7 8$ $9 $10$', discount=100)")
    calls.add("candidate(sentence='a' * 100000, discount=100)")
    calls.add("candidate(sentence='$9999999999', discount=1)")
    calls.add("candidate(sentence='$9999999999', discount=100)")
    while len(calls) < 600:
        words = []
        for _ in range(rng.randint(1, 12)):
            kind = rng.randrange(4)
            digits = str(rng.randint(1, 10**10 - 1))
            if kind == 0:
                words.append("$" + digits)
            elif kind == 1:
                words.append("$" + digits + rng.choice(string.ascii_lowercase))
            elif kind == 2:
                words.append(digits + "$")
            else:
                words.append(
                    "".join(
                        rng.choice(string.ascii_lowercase)
                        for _ in range(rng.randint(1, 8))
                    )
                )
        sentence = " ".join(words)
        discount = rng.randint(0, 100)
        calls.add(f"candidate(sentence={sentence!r}, discount={discount})")
    return sorted(calls)
