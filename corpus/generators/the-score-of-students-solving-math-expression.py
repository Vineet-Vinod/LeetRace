import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**data) -> None:
        s, a = data["s"], data["answers"]
        assert (
            3 <= len(s) <= 31
            and len(s) % 2 == 1
            and all(c in "0123456789" for c in s[::2])
            and all(c in "+*" for c in s[1::2])
        )
        assert 1 <= len(a) <= 10000 and all(0 <= x <= 1000 for x in a)
        # The mathematical precedence answer must satisfy the explicit promise.
        correct = 0
        for term in s.split("+"):
            product = 1
            for digit in term.split("*"):
                product *= int(digit)
            correct += product
        assert 0 <= correct <= 1000
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in data.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for example in [
        {"s": "7+3*1*2", "answers": [20, 13, 42]},
        {"s": "3+5*2", "answers": [13, 0, 10, 13, 13, 16, 16]},
        {"s": "6+0*1", "answers": [12, 9, 6, 4, 8, 6]},
    ]:
        add(**example)
    add(s="+".join("9" * 16), answers=[144] * 10000)
    add(s="9*9*9*9*9*9*9*0+1", answers=[0, 1, 9, 10, 1000])
    add(s="0*0", answers=[0] * 10000)
    while len(calls) < 600:
        count = rng.randint(2, 8)
        nums = [rng.randrange(10) for _ in range(count)]
        ops = [rng.choice("+*") for _ in range(count - 1)]
        s = "".join(
            str(nums[i]) + (ops[i] if i < len(ops) else "") for i in range(count)
        )
        correct = eval(s)
        if correct > 1000:
            continue
        # Include correct, common wrong left-associative, and unrelated answers.
        left = nums[0]
        for op, v in zip(ops, nums[1:]):
            left = left + v if op == "+" else left * v
        answers = [correct] * rng.randint(1, 5) + [
            rng.randrange(1001) for _ in range(rng.randint(1, 15))
        ]
        if left <= 1000:
            answers += [left] * rng.randint(1, 4)
        if len(calls) % 4 == 0:
            answers = [rng.randrange(1001) for _ in range(rng.randint(1, 20))]
        add(s=s, answers=answers)
    assert len(calls) == 600
    return calls
