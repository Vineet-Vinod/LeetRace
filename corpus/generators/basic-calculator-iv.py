import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        validate(kw)
        call = "candidate(" + ", ".join(k + "=" + repr(v) for k, v in kw.items()) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    def letters(n, alphabet="abc"):
        return "".join(rng.choice(alphabet) for _ in range(n))

    def tree(n, mode=0):
        edges = [
            [i, i - 1 if mode == 1 else 0 if mode == 2 else rng.randrange(i)]
            for i in range(1, n)
        ]
        labels = list(range(n))
        rng.shuffle(labels)
        edges = [[labels[a], labels[b]] for a, b in edges]
        rng.shuffle(edges)
        return edges

    def valid_tree(n, edges):
        assert len(edges) == n - 1
        parents = list(range(n))

        def root(x):
            while parents[x] != x:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x

        for a, b in edges:
            assert 0 <= a < n and 0 <= b < n and root(a) != root(b)
            parents[root(a)] = root(b)

    def lower(s):
        return all("a" <= c <= "z" for c in s)

    def validate(k):
        e = k["expression"]
        v = k["evalvars"]
        ints = k["evalints"]
        assert 1 <= len(e) <= 250 and e == e.strip() and "  " not in e
        assert all(c in "abcdefghijklmnopqrstuvwxyz0123456789+-*() " for c in e)
        assert (
            len(v) == len(ints) <= 100
            and all(1 <= len(x) <= 20 and lower(x) for x in v)
            and all(-100 <= x <= 100 for x in ints)
        )
        # Random expressions use small literals/variables and a bounded grammar.
        # Substitution magnitude <=100 and at most three factors keep intermediates within signed 32-bit bounds.

    add(expression="e + 8 - a + 5", evalvars=["e"], evalints=[1])
    add(
        expression="e - 8 + temperature - pressure",
        evalvars=["e", "temperature"],
        evalints=[1, 12],
    )
    add(expression="(e + 8) * (e - 8)", evalvars=[], evalints=[])
    add(expression=" + ".join(["aa"] + ["a"] * 62), evalvars=[], evalints=[])
    add(
        expression="a",
        evalvars=[letters(20) for _ in range(100)],
        evalints=[-100, 100] * 50,
    )
    add(expression="0", evalvars=[], evalints=[])
    add(expression="2147483647", evalvars=[], evalints=[])
    add(expression="0 - 2147483647 - 1", evalvars=[], evalints=[])
    add(expression="(a - a) * (b + 1)", evalvars=[], evalints=[])
    for expression in [
        "1 + 2 * 3",
        "a + b * c",
        "a * b + aa * c",
        "a - (b - c)",
        "a + b * c - b * c",
        "((a + b) * (a - b)) * (a + b)",
        " * ".join(["a"] * 31),
        "(a + b) * (c + d) * (aa + zz)",
    ]:
        add(expression=expression, evalvars=[], evalints=[])
        if expression != " * ".join(["a"] * 31):
            add(expression=expression, evalvars=["a", "b"], evalints=[-100, 100])
    while len(calls) < 600:
        variables = ["a", "b", "c", "temperature", "pressure"]

        def chunk():
            return rng.choice(variables + [str(rng.randrange(101))])

        e = chunk()
        for _ in range(rng.randrange(1, 6)):
            term = chunk()
            if rng.randrange(3) == 0:
                term = (
                    "(" + chunk() + " " + rng.choice(["+", "-"]) + " " + chunk() + ")"
                )
            e += " " + rng.choice(["+", "-"]) + " " + term
        if rng.randrange(3) == 0:
            e = "(" + e + ") * " + chunk()
        v = rng.sample(variables, rng.randrange(6))
        add(expression=e, evalvars=v, evalints=[rng.randint(-100, 100) for _ in v])
    assert len(calls) == 600 and len(set(calls)) == 600
    return calls
