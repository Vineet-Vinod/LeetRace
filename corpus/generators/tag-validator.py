import random
import string

EXAMPLES = [
    "candidate(code='<DIV>This is the first line <![CDATA[<div>]]></DIV>')",
    "candidate(code='<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>')",
    "candidate(code='<A>  <B> </A>   </B>')",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = list(EXAMPLES)
    seen = set(calls)

    def emit(call: str) -> None:
        if call not in seen:
            calls.append(call)
            seen.add(call)

    def add(code):
        assert 1 <= len(code) <= 500 and set(code) <= set(
            string.ascii_letters + string.digits + "<>/![]. "
        )
        emit(f"candidate(code={code!r})")

    add("<A>" + "x" * 493 + "</A>")
    add("x" * 500)
    add("<ABCDEFGHI></ABCDEFGHI>")
    add("<ABCDEFGHIJ></ABCDEFGHIJ>")

    def valid(depth):
        name = "".join(rng.choices(string.ascii_uppercase, k=rng.randint(1, 9)))
        inner = "".join(
            rng.choices(
                string.ascii_letters + string.digits + " >/.[]!", k=rng.randint(0, 12)
            )
        )
        if depth and rng.random() < 0.7:
            inner += valid(depth - 1)
        if rng.random() < 0.5:
            inner += (
                "<![CDATA["
                + "".join(rng.choices("<>/![]abcABC", k=rng.randint(0, 15)))
                + "]]>"
            )
        return "<" + name + ">" + inner + "</" + name + ">"

    while len(calls) < 600:
        code = valid(3)
        if rng.random() < 0.5:
            # Deliberate violations: text outside root, bad closing name, or multiple roots.
            code = rng.choice(
                [
                    "x" + code,
                    code + "x",
                    code + valid(1),
                    code.replace("</", "</z", 1),
                    code[:-1],
                    code.replace("<", "<a", 1),
                ]
            )
        if len(code) <= 500:
            add(code)
    return calls
