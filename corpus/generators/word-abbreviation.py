import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**data) -> None:
        a = data["words"]
        assert 1 <= len(a) <= 400 and len(set(a)) == len(a)
        assert all(
            2 <= len(w) <= 400 and set(w) <= set("abcdefghijklmnopqrstuvwxyz")
            for w in a
        )
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in data.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for example in [
        {
            "words": [
                "like",
                "god",
                "internal",
                "me",
                "internet",
                "interval",
                "intension",
                "face",
                "intrusion",
            ]
        },
        {"words": ["aa", "aaa"]},
    ]:
        add(**example)
    add(words=["a" * 400, "a" * 398 + "ba", "a" * 397 + "caa"])
    add(
        words=[
            "a" + chr(97 + i // 26) + chr(97 + i % 26) + "a" * 396 + "z"
            for i in range(400)
        ]
    )
    add(words=["aa"])
    while len(calls) < 600:
        n = rng.randint(1, 40)
        words = set()
        mode = len(calls) % 3
        while len(words) < n:
            if mode == 0:
                word = "abc" + "".join(rng.choice("abcxyz") for _ in range(5)) + "z"
            elif mode == 1:
                word = "".join(rng.choice("abc") for _ in range(rng.randint(2, 5)))
            else:
                word = "".join(
                    rng.choice("abcdefghijklmnopqrstuvwxyz")
                    for _ in range(rng.randint(2, 30))
                )
            words.add(word)
        add(words=sorted(words))
    assert len(calls) == 600
    return calls
