def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(num1='0',num2='123')", "candidate(num1='123',num2='456')"}
    while len(cases) < 600:

        def number() -> str:
            n = rng.randint(1, 200)
            return (
                "0"
                if n == 1 and rng.random() < 0.1
                else str(rng.randint(1, 9))
                + "".join(rng.choice("0123456789") for _ in range(n - 1))
            )

        a, b = number(), number()
        cases.add(f"candidate(num1={a!r},num2={b!r})")
    return sorted(cases)
