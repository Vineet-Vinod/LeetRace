import random
import string

EXAMPLES = [
    "candidate(expression='{a,b}{c,{d,e}}')",
    "candidate(expression='{{a,z},a{b,c},{ab,z}}')",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = list(EXAMPLES)
    seen = set(calls)

    def emit(call: str) -> None:
        if call not in seen:
            calls.append(call)
            seen.add(call)

    def add(s):
        assert 1 <= len(s) <= 60
        assert set(s) <= set(string.ascii_lowercase + "{},")
        # Construction recursively follows the union/concatenation grammar.
        emit(f"candidate(expression={s!r})")

    add("a" * 60)
    add("{a,b}" * 12)

    def expr(depth):
        if not depth or rng.random() < 0.35:
            return "".join(rng.choices("abcdef", k=rng.randint(1, 4)))
        if rng.random() < 0.6:
            return "{" + expr(depth - 1) + "," + expr(depth - 1) + "}"
        return expr(depth - 1) + expr(depth - 1)

    while len(calls) < 600:
        s = expr(3)
        if len(s) <= 60:
            add(s)
    return calls
