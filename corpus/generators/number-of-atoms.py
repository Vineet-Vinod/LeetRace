import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def emit(**values):
        formula = values["formula"]
        assert 1 <= len(formula) <= 1000
        # Validate the grammar and 32-bit atom totals independently of the golden parser.
        import re

        tokens = re.findall(r"[A-Z][a-z]*|[0-9]+|[()]", formula)
        assert "".join(tokens) == formula

        def parse(position, nested=False):
            totals = {}
            terms = 0
            while position < len(tokens) and tokens[position] != ")":
                token = tokens[position]
                if token == "(":
                    group, position = parse(position + 1, True)
                    assert tokens[position] == ")"
                    position += 1
                else:
                    assert token[0].isupper()
                    group = {token: 1}
                    position += 1
                multiplier = 1
                if position < len(tokens) and tokens[position].isdigit():
                    assert not tokens[position].startswith("0")
                    multiplier = int(tokens[position])
                    assert multiplier >= 2
                    position += 1
                for name, count in group.items():
                    totals[name] = totals.get(name, 0) + count * multiplier
                terms += 1
            assert terms and (nested or position == len(tokens))
            return totals, position

        totals, end = parse(0)
        assert end == len(tokens) and all(1 <= n <= 2**31 - 1 for n in totals.values())
        call = (
            "candidate("
            + ", ".join(name + "=" + repr(value) for name, value in values.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for formula in [
        "H",
        "H2O",
        "Mg(OH)2",
        "K4(ON(SO3)2)2",
        "H2147483647",
        "(" * 499 + "H" + ")" * 499,
        "H" * 1000,
        "Abcdefghijklmnopqrstuvwxyz",
    ]:
        emit(formula=formula)
    while len(calls) < 600:
        elements = ["H", "O", "Mg", "He", "Na", "Cl", "C", "N", "Xyz"]

        def formula(depth):
            parts = []
            for _ in range(rng.randint(1, 4)):
                term = (
                    "(" + formula(depth - 1) + ")"
                    if depth and rng.random() < 0.4
                    else rng.choice(elements)
                )
                term += str(rng.randint(2, 8)) if rng.random() < 0.5 else ""
                parts.append(term)
            return "".join(parts)

        emit(formula=formula(rng.randint(0, 3)))
    return calls
