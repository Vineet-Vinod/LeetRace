"""Seeded legal inputs, including original examples and maximum-size boundaries."""

import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def validate(kw):
        s = kw["s"]
        n = len(s)
        assert (
            2 <= n <= 100000
            and n % 2 == 0
            and all("a" <= c <= "z" for c in s)
            and 1 <= len(kw["queries"]) <= 100000
        )
        assert all(
            len(q) == 4 and 0 <= q[0] <= q[1] < n // 2 <= q[2] <= q[3] < n
            for q in kw["queries"]
        )

    def add_call(call):
        kw = eval(call, {"candidate": lambda **kwargs: kwargs})
        validate(kw)
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        if key not in seen:
            seen.add(key)
            calls.append(call)

    def factory(index):
        half = rng.randint(1, 40)
        left = "".join(rng.choices("abc", k=half))
        if index % 3 == 0:
            right = left[::-1]
        elif index % 3 == 1:
            values = list(left)
            rng.shuffle(values)
            right = "".join(values)
        else:
            right = "".join(rng.choices("abc", k=half))
        queries = []
        for _ in range(rng.randint(1, 15)):
            a, c = rng.randrange(half), rng.randrange(half)
            queries.append(
                [a, rng.randint(a, half - 1), half + c, half + rng.randint(c, half - 1)]
            )
        if index % 3 == 1:
            queries.append([0, half - 1, half, 2 * half - 1])
        return dict(s=left + right, queries=queries)

    for call in [
        'candidate(s = "abcabc", queries = [[1,1,3,5],[0,2,5,5]])',
        'candidate(s = "abbcdecbba", queries = [[0,2,7,9]])',
        'candidate(s = "acbcab", queries = [[1,2,4,5]])',
        "candidate(s='a'*100000,queries=[[0,49999,50000,99999]])",
        "candidate(s='a'*50000+'b'*50000,queries=[[0,49999,50000,99999]])",
        "candidate(s='ab',queries=[[0,0,1,1]]*100000)",
    ]:
        add_call(call)
    index = 0
    while len(calls) < 600:
        kw = factory(index)
        add_call(
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kw.items())
            + ")"
        )
        index += 1
    assert len(calls) == len(set(calls)) == 600
    return calls
