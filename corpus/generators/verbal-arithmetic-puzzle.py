import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def emit(**values):
        words, result = values["words"], values["result"]
        assert 2 <= len(words) <= 5 and all(
            1 <= len(w) <= 7 and w.isascii() and w.isalpha() and w.isupper()
            for w in words + [result]
        )
        assert len(set("".join(words) + result)) <= 10
        call = (
            "candidate("
            + ", ".join(name + "=" + repr(value) for name, value in values.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    emit(words=["SEND", "MORE"], result="MONEY")
    emit(
        words=["BCDEFGH", "BACDEFG", "BABCDEG", "BABCDEF", "BABCDEH"], result="FCJFAGB"
    )
    emit(words=["SIX", "SEVEN", "SEVEN"], result="TWENTY")
    emit(words=["LEET", "CODE"], result="POINT")
    emit(words=["AAAAAAA"] * 5, result="BBBBBBB")
    emit(words=["ABCDEFG", "ABCDEFG"], result="HIJ")
    while len(calls) < 600:
        mode = len(calls) % 2
        if mode == 0:
            count = rng.randint(2, 5)
            numbers = [rng.randint(0, 999) for _ in range(count)]
            digits = list("ABCDEFGHIJ")
            rng.shuffle(digits)

            def encode(n):
                return "".join(digits[int(c)] for c in str(n))

            emit(words=[encode(n) for n in numbers], result=encode(sum(numbers)))
        else:
            alphabet = "ABC" if len(calls) % 4 == 1 else "ABCD"
            words = [
                "".join(rng.choices(alphabet, k=rng.randint(1, 4)))
                for _ in range(rng.randint(2, 5))
            ]
            result = "".join(rng.choices(alphabet, k=rng.randint(1, 5)))
            emit(words=words, result=result)
    return calls
