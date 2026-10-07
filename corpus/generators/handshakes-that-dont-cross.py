import random

DOMAIN_SIZE = 500


def generate(seed: int = 0) -> list[str]:
    random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        assert 2 <= kw["numPeople"] <= 1000 and kw["numPeople"] % 2 == 0
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kw.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for kw in [{"numPeople": 4}, {"numPeople": 6}] + []:
        add(**kw)
    for n in range(2, 1001, 2):
        add(numPeople=n)
    return calls
