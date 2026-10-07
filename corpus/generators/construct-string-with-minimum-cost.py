import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        validate(**kwargs)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        calls[call] = None

    def validate(target, words, costs):
        assert 1 <= len(target) <= 50000 and 1 <= len(words) == len(costs) <= 50000
        assert sum(map(len, words)) <= 50000 and all(
            1 <= len(w) <= len(target) for w in words
        )
        assert all(
            set(w) <= set("abcdefghijklmnopqrstuvwxyz") for w in [target] + words
        )
        assert all(1 <= c <= 10000 for c in costs)

    add(
        target="abcdef",
        words=["abdef", "abc", "d", "def", "ef"],
        costs=[100, 1, 1, 10, 5],
    )
    while len(calls) < 597:
        target = "".join(rng.choices("abc", k=rng.randint(1, 35)))
        words = [
            "".join(rng.choices("abc", k=rng.randint(1, min(8, len(target)))))
            for _ in range(rng.randint(1, 15))
        ]
        if len(calls) % 3 == 0:
            words += sorted(set(target))
        if len(calls) % 3 == 1:
            words = [w.replace("a", "z") for w in words]
            target = "a" + target[1:]
        costs = [rng.randint(1, 10000) for _ in words]
        add(target=target, words=words, costs=costs)
    calls['candidate(target="a"*50000, words=["a"], costs=[10000])'] = None
    calls['candidate(target="a"*50000, words=["a"*50000], costs=[1])'] = None
    calls['candidate(target="a", words=["a"]*50000, costs=[10000]*49999+[1])'] = None
    # Also validate the evaluated compact expressions used for maximum boundaries.
    for call in calls:
        eval(call, {"candidate": validate})
    return list(calls)
