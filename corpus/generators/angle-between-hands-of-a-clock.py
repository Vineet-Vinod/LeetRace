def generate(seed: int = 0) -> list[str]:
    import random

    random.Random(seed)
    cases = {
        f"candidate(hour={hour}, minutes={minute})"
        for hour in range(1, 13)
        for minute in range(60)
    }
    # The full valid input domain has 720 distinct calls and is exhaustively enumerated.
    return sorted(cases)
