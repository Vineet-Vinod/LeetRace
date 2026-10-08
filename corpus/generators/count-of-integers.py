import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(num1: str, num2: str, min_sum: int, max_sum: int) -> None:
        assert (
            num1.isdigit()
            and num2.isdigit()
            and str(int(num1)) == num1
            and str(int(num2)) == num2
        )
        assert 1 <= int(num1) <= int(num2) <= 10**22
        assert 1 <= min_sum <= max_sum <= 400
        call = (
            "candidate("
            + ", ".join(
                f"{key}={value!r}"
                for key, value in [
                    ("num1", num1),
                    ("num2", num2),
                    ("min_sum", min_sum),
                    ("max_sum", max_sum),
                ]
            )
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(num1="1", num2="12", min_sum=1, max_sum=8)
    add(num1="1", num2=str(10**22), min_sum=1, max_sum=400)
    add(num1=str(10**22), num2=str(10**22), min_sum=400, max_sum=400)
    add(num1="1", num2="12", min_sum=1, max_sum=8)
    add(num1="1", num2="5", min_sum=1, max_sum=5)
    while len(calls) < 600:
        a = rng.randint(1, 10000)
        b = a + rng.randint(0, 20000)
        if len(calls) % 6 == 0:
            a = rng.randint(1, 10**20)
            b = rng.randint(a, 10**22)
        lo = rng.randint(1, 50)
        hi = rng.choice([lo, rng.randint(lo, 400)])
        add(num1=str(a), num2=str(b), min_sum=lo, max_sum=hi)
    return calls
