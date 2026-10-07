import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        validate(**kwargs)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        calls[call] = None

    def validate(s, wordDict):
        assert (
            1 <= len(s) <= 20
            and 1 <= len(wordDict) <= 1000
            and len(set(wordDict)) == len(wordDict)
        )
        assert all(
            1 <= len(w) <= 10 and set(w) <= set("abcdefghijklmnopqrstuvwxyz")
            for w in wordDict
        ) and set(s) <= set("abcdefghijklmnopqrstuvwxyz")
        # Independent count DP enforces promised number of sentences <= 10^5.
        counts = [1] + [0] * len(s)
        words = set(wordDict)
        for end in range(1, len(s) + 1):
            counts[end] = sum(
                counts[start]
                for start in range(max(0, end - 10), end)
                if s[start:end] in words
            )
        assert counts[-1] <= 100000

    add(s="catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"])
    add(
        s="pineapplepenapple",
        wordDict=["apple", "pen", "applepen", "pine", "pineapple"],
    )
    add(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"])
    while len(calls) < 597:
        s = "".join(rng.choices("abc", k=rng.randint(1, 20)))
        words = {
            "".join(rng.choices("abc", k=rng.randint(1, 10)))
            for _ in range(rng.randint(1, 20))
        }
        if len(calls) % 3 == 0:
            words.update(s)
        if len(calls) % 3 == 1:
            s = "z" + s[1:]
        add(s=s, wordDict=sorted(words))
    add(s="a" * 20, wordDict=["a", "aa"])
    add(s="a" * 20, wordDict=["a" * 10])
    # 1000 unique length-10 binary words; no sentence explosion for this target.
    add(
        s="c" * 20,
        wordDict=[
            format(i, "010b").replace("0", "a").replace("1", "b") for i in range(1000)
        ],
    )
    # Also validate the evaluated compact expressions used for maximum boundaries.
    for call in calls:
        eval(call, {"candidate": validate})
    return list(calls)
